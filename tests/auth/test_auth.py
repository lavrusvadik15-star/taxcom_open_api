import json
from http import HTTPStatus

import allure
import pytest

from clients.auth.auth_client import AuthClient, PrivateAuthClient
from clients.auth.auth_schema import LoginRequestSchema, LoginResponseSchema, LoginCertificateRequestSchema, \
    LoginCertificateResponseSchema
from fixtures.auth import public_auth_client
from tools.allure_utils.tags import AllureTags
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

    @allure.title("Login with correct employee")
    def test_login_employee(self, public_auth_client: AuthClient):
        login_request = LoginRequestSchema(
            login="dfghxs@yandex.ru",
            password="722b0a4c-b162-4d26-b1e8-1955a707a338"
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

    @allure.title("Login with cetrificate")
    def test_login_with_certificate(self,
                                    public_auth_client: AuthClient,
                                    certificate_base64_str: str
                                    ):
        login_request = LoginCertificateRequestSchema(
                is_cert_new_qes= True,
                is_cloud=None,
                abonent_id="8260214A-2575-45DF-9E56-657D5B4810B8",
                email=None,
                certificate_public_key= certificate_base64_str)
        login_reponse = public_auth_client.login_certificate_api(login_request)
        response_string = login_reponse.content.decode('utf-8')
        response_data = LoginCertificateResponseSchema.model_validate_json(response_string)
        print(response_data)

    @allure.title("Get abonent permission")
    def test_abonent_permission(self, private_auth_client: PrivateAuthClient):
        response = private_auth_client.get_abonent_permission()
        #Статус код
        assert_status_code(response.status_code, HTTPStatus.OK)


    def test_abonent_permission2(self, private_auth_cert_client: PrivateAuthClient):
        response = private_auth_cert_client.get_abonent_permission()
        #Статус код
        print(response.text)