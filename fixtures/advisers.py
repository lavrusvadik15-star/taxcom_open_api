import pytest

from clients.advisers.advisers_client import AdvisersClient, get_advisers_client
from fixtures.auth import CabinetSchema


@pytest.fixture
def advisers_client(auth_cabinet: CabinetSchema) -> AdvisersClient :
    """Создаем клиент для advissers от фикструы авторизации по кредам кабинета"""
    return get_advisers_client(auth_cabinet.credentials)