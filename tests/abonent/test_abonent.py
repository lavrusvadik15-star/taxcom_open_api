from http import HTTPStatus

import allure
import pytest

from clients.abonent import abonent_client
from clients.abonent.abonent_client import AbonentClient
from clients.abonent.abonent_schema import GetAbonentRequest, GetAbonentResponseSchema, \
    GetAbonentRequisitesResponseSchema, AvailableDepartmentsResponseSchema, GetMobileQRResponseSchema, \
    GetAutopilotStatusResponseSchema
from fixtures.auth import CabinetSchema
from tools.allure.tags import AllureTags
from tools.assertions.abonent import assert_abonent_requisites, assert_available_departments, assert_get_mobile_qr, \
    assert_get_autopilot_status
from tools.assertions.base import assert_status_code
from tools.assertions.json import validate_json_schema


@pytest.mark.regression
@pytest.mark.abonent
@allure.tag(AllureTags.ABONENT, AllureTags.REGRESSION)
class TestAbonent:
    @allure.title("Get abonent")
    #РАЗОБРАТЬСЯ ПОЧЕМУ NULL ПРИХОДИТ В КАБИНЕТ ОВНЕРЕ и тест абонент FALSE? БАГ?
    def test_get_abonent(self,
                         abonent_client: AbonentClient,
                         auth_cabinet: CabinetSchema):
        #abonents_id = auth_cabinet.response.abonents[0].id
        query = GetAbonentRequest(abonent_id= auth_cabinet.response.abonents[0].id)
        #запрос
        response = abonent_client.get_abonent(query)
        # Декодируем пришедшую байтовую строку байтовой строку в обычную строку
        response_string = response.content.decode('utf-8')
        # Десериализация JSON-ответа в объект
        response_string_data = GetAbonentResponseSchema.model_validate_json(response_string)
        #статус код проверка
        assert_status_code(response.status_code, HTTPStatus.OK)

    @allure.title("Get abonent requisites")
    def test_get_abonent_requisites(self, abonent_client: AbonentClient, auth_cabinet: CabinetSchema):
        query = GetAbonentRequest(abonent_id= auth_cabinet.response.abonents[0].id)
        # запрос
        response = abonent_client.get_abonent_requisites(query)
        # Декодируем пришедшую байтовую строку байтовой строку в обычную строку
        response_string = response.content.decode('utf-8')
        #Десериализация JSON-ответа в объект
        response_string_data = GetAbonentRequisitesResponseSchema.model_validate_json(response_string)
        #статус код проверка
        assert_status_code(response.status_code, HTTPStatus.OK)
        #проверяем что ответ не пустой (тут только инн в проверке, можно добавить больше полей если нужно)
        assert_abonent_requisites(response_string_data)

        # Дополнительно проверяем, что тело ответа сервера соответствует ожидаемой JSON-схеме
        validate_json_schema(response.json(),response_string_data.model_json_schema())

    @allure.title("Get available departments")
    def test_available_departments(self, abonent_client: AbonentClient, auth_cabinet: CabinetSchema):
        query = GetAbonentRequest(abonent_id=auth_cabinet.response.abonents[0].id)
        #запрос
        response = abonent_client.available_departments(query)
        # Декодируем пришедшую байтовую строку байтовой строку в обычную строку
        response_string = response.content.decode('utf-8')
        # #Десериализация JSON-ответа в объект
        response_string_data = AvailableDepartmentsResponseSchema.model_validate_json(response_string)
        # статус код
        assert_status_code(response.status_code, HTTPStatus.OK)
        # Валидация что ответ содержит список
        assert_available_departments(response_string_data)

    @allure.title("Get mobile QR")
    def test_get_mobile_qr(self,abonent_client: AbonentClient):
        # ЗАпрос
        response = abonent_client.get_mobile_qr()
        #print(response.)
        # Диссериализация в объект (возьмем как текст просто, там 1 строка в ответе)
        response_data = GetMobileQRResponseSchema.model_validate_json(response.text)
        #статус код
        assert_status_code(response.status_code, HTTPStatus.OK)
        #Валидацяи наличия тела ответа
        assert_get_mobile_qr(response_data)

        # Дополнительно проверяем, что тело ответа сервера соответствует ожидаемой JSON-схеме
        validate_json_schema(response.json(),response_data.model_json_schema())

    @allure.title("Get autopilot status")
    def test_get_autopilot_status(self, abonent_client: AbonentClient):
        #Запрос
        response = abonent_client.get_autopilot_status()
        # Диссериализация в объект
        response_data = GetAutopilotStatusResponseSchema.model_validate_json(response.content)
        #Проверим, что ответ не пуст и булево значение
        assert_get_autopilot_status(response_data)

        # Дополнительно проверяем, что тело ответа сервера соответствует ожидаемой JSON-схеме
        validate_json_schema(response.json(),response_data.model_json_schema())







