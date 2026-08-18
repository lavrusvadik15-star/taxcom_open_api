import pytest

from clients.abonent.abonent_client import AbonentClient, get_abonent_client, get_abonent_cert_client
from clients.auth.auth_client import PrivateAuthClient
from fixtures.auth import CabinetSchema


@pytest.fixture
def abonent_client(auth_cabinet: CabinetSchema) -> AbonentClient:
    """Создаем клиент для abonent от фикструы авторизации по кредам кабинета"""
    return get_abonent_client(auth_cabinet.credentials)



@pytest.fixture
def abonent_cert_client(private_auth_cert_client: PrivateAuthClient) -> AbonentClient:
    """Создаем фикстуру создания клиента от фикструы авторизации по серту"""
    #return DepartmentClient(client=private_auth_cert_client.client)
    return get_abonent_cert_client(http_client=private_auth_cert_client.client)
