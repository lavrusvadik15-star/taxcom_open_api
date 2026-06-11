import pytest
from pydantic import BaseModel

from clients.department.department_client import DepartmentClient, get_department_client
from clients.department.department_schema import DepartmentListSchema, GetListDepartmentsResponseSchema
from fixtures.auth import CabinetSchema


@pytest.fixture
def department_client(auth_cabinet: CabinetSchema) -> DepartmentClient:
    """Создаем фикстуру создания клиента от фикструы авторизации по кредам кабинета"""
    return get_department_client(auth_cabinet.credentials)


class Department(BaseModel):
    response: GetListDepartmentsResponseSchema
    #возьмем айди первого из массива (головное есть всегда)
    @property
    def get_department_id(self) -> str:
        department_id = self.response.infos[0].id
        return (department_id)

@pytest.fixture
def list_departments(department_client: DepartmentClient) -> Department:
    response = department_client.get_list_departments()
    response_data = GetListDepartmentsResponseSchema.model_validate_json(response.text)
    return Department(response= response_data)