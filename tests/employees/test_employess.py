import pytest
import allure

from clients.employees.employees_client import EmployeesClient
from tools.allure.tags import AllureTags


@pytest.mark.regression
@pytest.mark.employees
@allure.tag(AllureTags.EMPLOYEES, AllureTags.REGRESSION)
class TestEmployees:
    """Класс для тестирования сотрудников"""

    def test_get_list_employees(self, employees_client: EmployeesClient):
        response= employees_client.get_list_employees()
        print(response.text)