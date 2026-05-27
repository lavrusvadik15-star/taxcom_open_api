import json
from http import HTTPStatus

import allure
import pytest

from clients.auth.auth_client import AuthClient, PrivateAuthClient
from clients.auth.auth_schema import LoginRequestSchema, LoginResponseSchema, LoginCertificateRequestSchema
from fixtures.auth import public_auth_client
from tools.allure.tags import AllureTags
from tools.assertions.auth import assert_login_response, assert_login_response_access_denied
from tools.assertions.base import assert_status_code
from tools.assertions.json import validate_json_schema
from tools.fakers import fake


@pytest.mark.regression
@pytest.mark.auth
@allure.tag(AllureTags.AUTH, AllureTags.REGRESSION)
class TestAuth:
    @allure.title("Login with correct email and password")
    def test_login_cabinet(self,
                   public_auth_client: AuthClient):

        login_request = LoginRequestSchema(
            login="ad9511df-5507-44be-96ae-ddc8410ae38c",
            password="kR1Zd1WoWdMdpTvWfkxx"
        )
        # Авторизация через API по кредам
        login_response = public_auth_client.login_api(login_request)
        # Декодируем пришедшую байтовую строку байтовой строку в обычную строку
        json_string_response = login_response.content.decode('utf-8')
        # преобразование строки JSON в словарь, но тут не надо, кажется
        #data = json.loads(json_string_response)
        # Десериализация JSON-ответа в объект LoginResponseSchema
        login_response_data = LoginResponseSchema.model_validate_json(json_string_response)
        #статус код проверка
        assert_status_code(login_response.status_code, HTTPStatus.OK)
        #проверка тела ответа
        assert_login_response(login_response_data)

        # Дополнительно проверяем, что тело ответа сервера соответствует ожидаемой JSON-схеме
        validate_json_schema(login_response.json(),login_response_data.model_json_schema())

    @allure.title("Login with incorrect abonent id")
    def test_login_cabinet_invalide(self,
                                    public_auth_client: AuthClient):
        login_request = LoginRequestSchema(
            login="ad9511df-5507-44be-96ae-ddc8410ae38c",
            password="kR1Zd1WoWdMdpTvWfkxx",
            abonent_id=fake.uuid()
        )
        # Авторизация через API по кредам
        login_response = public_auth_client.login_api(login_request)
        # Декодируем пришедшую байтовую строку байтовой строку в обычную строку
        json_string_response = login_response.content.decode('utf-8')
        # Десериализация JSON-ответа в объект LoginResponseSchema
        login_response_data = LoginResponseSchema.model_validate_json(json_string_response)
        #Статус код
        assert_status_code(login_response.status_code, HTTPStatus.OK)
        # Проверка ответа
        assert_login_response_access_denied(login_response_data)


    # # Не вышло никаким образом извлечь данные из серта, чтобы передавать их как параметр
    # @allure.title("Login with cetrificate")
    # def test_login_with_certificate(self,
    #                                 public_auth_client: AuthClient
    #                                 ):
    #     pass
    #     # login_request = LoginCertificateRequestSchema(
    #     #         is_cert_new_qes=True,
    #     #         is_cloud=None,
    #     #         abonent_id=None,
    #     #         email=None,
    #     #         certificatePublicKey= "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"
    #     # )
    #     # # Авторизация через API по кредам
    #     # login_response = auth_client.login_api(login_request)
    #     # print(login_response)

    @allure.title("Get abonent permission")
    def test_abonent_permission(self, private_auth_client: PrivateAuthClient):
        response = private_auth_client.get_abonent_permission()
        #Статус код
        assert_status_code(response.status_code, HTTPStatus.OK)