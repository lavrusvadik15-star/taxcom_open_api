from clients.employees.employees_client import EmployeesClient, get_employees_client
from fixtures.auth import CabinetSchema
import pytest

@pytest.fixture
def employees_client(auth_cabinet: CabinetSchema) -> EmployeesClient:
    """Фикстура создания клиента сотрудников от фикструры авторизации"""
    return get_employees_client(auth_cabinet.credentials)