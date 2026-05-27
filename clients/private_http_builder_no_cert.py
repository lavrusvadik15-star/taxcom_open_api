from functools import lru_cache

from httpx import Client
from pydantic import BaseModel

from clients.auth.auth_schema import LoginRequestSchema


# Структура данных пользователя для авторизации.
# Создали заново, а не взяли из LoginRequestDict - потому что билдер должен быть независим от апи клиентов
# frozen=True Добавлено для хеширования аргумента (красное, потому что это косяк python самого, не влияет)
class AuthenticationUserSchema(BaseModel, frozen=True):
    login: str
    password: str

# Создаем private builder
# Это импортировано из библиотеки functools. Позволяет кешировать. (maxsize=None) - количество кеширований
# Но требует, чтобы передаваемые аргументы были хешируемые (т.е. не изменяемые. Мы это сделаем аргументом frozen=True в схеме)
@lru_cache(maxsize=None)
def get_private_http_client_no_cert(user: AuthenticationUserSchema) -> Client:
    """
    Функция создаёт экземпляр httpx.Client с аутентификацией пользователя.

    :param user: Объект AuthenticationUserSchema с email и паролем пользователя.
    :return: Готовый к использованию объект httpx.Client с установленным заголовком Authorization.
    """
    # Импортируем внутри функции, чтобы избежать циклического импорта
    from clients.auth.auth_client import get_auth_client

    auth_client = get_auth_client()
    login_request = LoginRequestSchema(
        login="ad9511df-5507-44be-96ae-ddc8410ae38c",
        password="kR1Zd1WoWdMdpTvWfkxx"
    )
    # Авторизация через API по кредам
    login_response = auth_client.login(login_request)

    return Client(
        timeout=100,
        base_url="http://stage-web:57000",
        # Добавляем заголовок авторизации, который мы заберем из ответа login(выше). Получается пирамида обратная
        headers={"Authorization": f"Bearer {login_response.token}"}
    )