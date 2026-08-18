import pytest

from clients.auth.auth_client import PrivateAuthClient
from clients.document.document_client import DocumentClient, get_document_client, get_document_cert_client
from fixtures.auth import CabinetSchema


@pytest.fixture
def document_client(auth_cabinet: CabinetSchema) -> DocumentClient:
    """Создаем фикстуру создания клиента от фикструы авторизации по кредам кабинета"""
    return get_document_client(auth_cabinet.credentials)


@pytest.fixture
def document_cert_client(private_auth_cert_client: PrivateAuthClient) -> DocumentClient:
    """Создаем фикстуру создания клиента от фикструы авторизации по серту"""
    #return DepartmentClient(client=private_auth_cert_client.client)
    return get_document_cert_client(http_client=private_auth_cert_client.client)