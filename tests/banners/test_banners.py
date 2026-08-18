from http import HTTPStatus

import pytest
import allure
import json

from clients.banners.banners_client import BannersClient
from clients.banners.banners_schema import GetBannersResponseSchema
from tools.allure_utils.tags import AllureTags
from tools.assertions.banners import assert_get_banners
from tools.assertions.base import assert_status_code
from tools.assertions.json import validate_json_schema


@pytest.mark.regression
@pytest.mark.contacts
@allure.tag(AllureTags.BANNERS, AllureTags.REGRESSION)
class TestBanners:
    """Класс для тестирования баннеров"""
    @allure.title("Get banners")
    def test_get_banners(self, banners_client: BannersClient):
        #запрос
        response = banners_client.get_banners()

        # тут возвращает массив, а не объект, потому преобразуем JSON‑массив в объект нашей схемы
        raw_data = json.loads(response.text)  # парсим JSON в Python‑структуру
        wrapped_data = {"banners": raw_data}  # оборачиваем массив в объект
        json_wrapped = json.dumps(wrapped_data)  # снова преобразуем в JSON‑строку

        response_data = GetBannersResponseSchema.model_validate_json(json_wrapped)

        #статус код
        assert_status_code(response.status_code, HTTPStatus.OK)
        #Проверка данных в массиве или его пустоты
        assert_get_banners(response_data)

        # Дополнительно проверяем, что тело ответа сервера соответствует ожидаемой JSON-схеме
        validate_json_schema(wrapped_data, response_data.model_json_schema())
