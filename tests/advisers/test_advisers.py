import allure
import pytest
import json

from clients.advisers.advisers_client import AdvisersClient
from clients.advisers.advisers_schema import GetAdvisersResponseSchema
from tools.allure.tags import AllureTags


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
