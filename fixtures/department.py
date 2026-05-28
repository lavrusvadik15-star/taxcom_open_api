import pytest

from clients.department.department_client import DepartmentClient, get_department_client
from fixtures.auth import CabinetSchema


@pytest.fixture
def department_client(auth_cabinet: CabinetSchema) -> DepartmentClient:
    """Создаем фикстуру создания клиента от фикструы авторизации по кредам кабинета"""
    return get_department_client(auth_cabinet.credentials)