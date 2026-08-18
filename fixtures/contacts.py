import pytest

from clients.auth.auth_client import PrivateAuthClient
from clients.contacts.contact_client import get_contacts_client, ContactClient, get_contacts_cert_client
from fixtures.auth import CabinetSchema


@pytest.fixture
def contacts_client(auth_cabinet: CabinetSchema) -> ContactClient:
    """Создаем фикстуру создания клиента от фикструы авторизации по кредам кабинета"""
    return get_contacts_client(auth_cabinet.credentials)


@pytest.fixture
def contacts_cert_client(private_auth_cert_client: PrivateAuthClient) -> ContactClient:
    """Создаем фикстуру создания клиента от фикструы авторизации по серту"""
    #return DepartmentClient(client=private_auth_cert_client.client)
    return get_contacts_cert_client(http_client=private_auth_cert_client.client)