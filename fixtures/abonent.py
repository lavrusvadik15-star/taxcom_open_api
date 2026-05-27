import pytest

from clients.abonent.abonent_client import AbonentClient, get_abonent_client
from fixtures.auth import CabinetSchema


@pytest.fixture
def abonent_client(auth_cabinet: CabinetSchema) -> AbonentClient:
    """Создаем клиент для abonent от фикструы авторизации по кредам кабинета"""
    return get_abonent_client(auth_cabinet.credentials)