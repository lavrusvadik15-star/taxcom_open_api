from http import HTTPStatus

import allure
import pytest
import json

from clients.advisers.advisers_client import AdvisersClient
from clients.advisers.advisers_schema import GetAdvisersResponseSchema, SubscribeAdvisersRequestSchema, \
    UnsubscribeAdvisersRequestSchema, GetAdviserSubscriptionResponseSchema
from fixtures.advisers import Advisers
from tools.allure_utils.tags import AllureTags
from tools.assertions.advisers import assert_advisers_subscription, assert_get_advisers
from tools.assertions.base import assert_status_code
from tools.assertions.json import validate_json_schema


@pytest.mark.regression
@pytest.mark.advisers
@allure.tag(AllureTags.ADVISERS, AllureTags.REGRESSION)
class TestAdvisor:
    @allure.title("Get advisor")
    def test_get_advisor(self, advisers_client: AdvisersClient):
        #запрос
        response = advisers_client.get_advisers()
        #декодируем
        response_string = response.content.decode('utf-8')

        # тут возвращает массив, а не объект, потому преобразуем JSON‑массив в объект нашей схемы
        raw_data = json.loads(response_string)  # парсим JSON в Python‑структуру
        wrapped_data = {"advisers": raw_data}  # оборачиваем массив в объект
        json_wrapped = json.dumps(wrapped_data)  # снова преобразуем в JSON‑строку

        #преобразуем в объект по схеме
        response_data = GetAdvisersResponseSchema.model_validate_json(json_wrapped)

        #Статус код
        assert_status_code(response.status_code, HTTPStatus.OK)
        #Проверка каждого элемента или пустоты массива
        assert_get_advisers(response_data)

        # Дополнительно проверяем, что тело ответа сервера соответствует ожидаемой JSON-схеме
        validate_json_schema(wrapped_data,response_data.model_json_schema())


    @allure.title("Subscribe adviser")
    def test_subscribe_adviser(self, advisers_client: AdvisersClient, get_adviser: Advisers):
        request = SubscribeAdvisersRequestSchema(adviser_id=get_adviser.get_advisers_id)
        #запрос
        response = advisers_client.subscribe_adviser(request)
        #статус код
        assert_status_code(response.status_code, HTTPStatus.OK)

    @allure.title("Unsubscribe adviser")
    def test_unsubscribe_adviser(self, advisers_client: AdvisersClient):
        request = UnsubscribeAdvisersRequestSchema()
        #Запрос
        response = advisers_client.unsubcribe_adviser(request)
        #Статус код
        assert_status_code(response.status_code, HTTPStatus.OK)

    @allure.title("Get Adviser Subscription")
    def test_get_adviser_subscription(self, advisers_client: AdvisersClient):
        # Запрос
        response = advisers_client.get_adviser_subscription()

        # тут возвращает массив, а не объект, потому преобразуем JSON‑массив в объект нашей схемы
        raw_data = json.loads(response.text)  # парсим JSON в Python‑структуру
        wrapped_data = {"adviser": raw_data}  # оборачиваем массив в объект
        json_wrapped = json.dumps(wrapped_data)  # снова преобразуем в JSON‑строку

        response_data = GetAdviserSubscriptionResponseSchema.model_validate_json(json_wrapped)
        # Статутс кода
        assert_status_code(response.status_code, HTTPStatus.OK)
        # Проверим что там массив, и если не пустой - то его данные
        assert_advisers_subscription(response_data)

        # Дополнительно проверяем, что тело ответа сервера соответствует ожидаемой JSON-схеме
        validate_json_schema(wrapped_data,response_data.model_json_schema())


