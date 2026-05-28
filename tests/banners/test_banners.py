from http import HTTPStatus

import pytest
import allure

from clients.banners.banners_client import BannersClient
from tools.allure.tags import AllureTags
from tools.assertions.base import assert_status_code


@pytest.mark.regression
@pytest.mark.banners
@allure.tag(AllureTags.BANNERS, AllureTags.REGRESSION)
class TestBanners:
    """Класс для тестирования баннеров"""
    @allure.title("Get banners")
    def test_get_banners(self, banners_client: BannersClient):
        #запрос
        response = banners_client.get_banners()

        #статус код
        assert_status_code(response.status_code, HTTPStatus.OK)
