import json

import pytest
from pydantic import BaseModel

from clients.department.department_client import DepartmentClient, get_department_client
from clients.department.department_schema import DepartmentListSchema, GetListDepartmentsResponseSchema, \
    CreateDepartmentRequestSchema, CreateDepartmentResponseSchema
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

class NewDepartment(BaseModel):
    response: CreateDepartmentResponseSchema
    #Берем id созданного департамента
    @property
    def get_new_department_id(self) -> str:
        new_department_id=self.response.department_id
        return (new_department_id)


@pytest.fixture
def list_departments(department_client: DepartmentClient) -> Department:
    """Фикстура получения списка департментов"""
    response = department_client.get_list_departments()
    response_data = GetListDepartmentsResponseSchema.model_validate_json(response.text)
    return Department(response= response_data)

@pytest.fixture
def create_department(department_client: DepartmentClient, list_departments: Department) -> NewDepartment:
    """Фикстура для создания нового подразделения"""
    request = CreateDepartmentRequestSchema(parent_department_id=list_departments.get_department_id)
    response = department_client.create_new_department(request)
    # Т.к. в ответе просто приходится id нового департамента, то обернем его
    raw_data = json.loads(response.content)
    wrapped_data = {"department_id": raw_data}  # оборачиваем массив в объект
    json_wrapped = json.dumps(wrapped_data)  # снова преобразуем в JSON‑строку
    response_data = CreateDepartmentResponseSchema.model_validate_json(json_wrapped)
    return NewDepartment(response= response_data)