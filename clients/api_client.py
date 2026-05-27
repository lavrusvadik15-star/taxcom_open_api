from typing import Any
import allure
from httpx import Client, URL, QueryParams, Response
from httpx._types import RequestData, RequestFiles


#Тут базовый апи клиент возможных типов запросов и что они принимают
class ApiClient:
    #это интерфес по какому принципу необходимо инициализировать все наши апи клиент
    #для каждого надо передать на вход клиент httpx
    def __init__(self, client: Client):
        """
        Базовый API клиент, принимающий объект httpx.Client.
        :param client: экземпляр httpx.Client для выполнения HTTP запросов
        """
        self.client = client

    @allure.step("Make GET request to {url}")
    def get(self, url: URL | str, params: QueryParams | None = None) -> Response:
        """
        Выполняет GET-запрос.
        :param url: URL-адрес эндпоинта.
        :param params: GET параметры запроса. Либо параметры в строке, либо ничего. По умолчанию =ничего.
        :return: Объект Response с данными ответа.
        """
        return self.client.get(url, params=params)

    @allure.step("Make POST request to {url}")
    def post(self, url: URL | str,
             json: Any | None = None,
             data: RequestData | None = None,
             files: RequestFiles | None = None,
             params: QueryParams | None = None
             ) -> Response:
        """ Выполняет POST-запрос.
        :param url: URL адрес.
        :param json: Данные в формате JSON.
        :param data: Форматированные данные формы.
        :param files: Файлы.
        :param params: Гет-параметры Либо параметры в строке, либо ничего. По умолчанию =ничего. !!!
        :return: Объект Response с данными ответа."""
        return self.client.post(url, json=json, data=data, files=files, params=params)

    @allure.step("Make DELETE request to {url}")
    def delete(self, url: URL | str) -> Response:
        """
        Выполняет DELETE запрос.
        :param url: URL адрес.
        :return: Объект Response с данными ответа.
        """
        return self.client.delete(url)

    @allure.step("Make PATCH request to {url}")
    def patch (self, url: URL | str, json: Any | None = None) -> Response:
        """ хз есть ли он, можно будет добавить по надобности"""
        ...

