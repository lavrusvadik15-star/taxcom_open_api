import json

from pydantic import BaseModel

from clients.auth.auth_client import PrivateAuthClient
from clients.employees.employees_client import EmployeesClient, get_employees_client, get_employees_cert_client
from clients.employees.employees_schema import CreateEmployeeRequestSchema, CreateEmployeeResponseSchema, \
    GetEmployeeRequestSchema, GetEmployeeResponseSchema, DeleteEmployeeRequestSchema
from fixtures.auth import CabinetSchema
import pytest

from fixtures.department import Department


@pytest.fixture
def employees_client(auth_cabinet: CabinetSchema) -> EmployeesClient:
    """Фикстура создания клиента сотрудников от фикструры авторизации"""
    return get_employees_client(auth_cabinet.credentials)

@pytest.fixture
def employees_cert_client(private_auth_cert_client: PrivateAuthClient) -> EmployeesClient:
    """Создаем фикстуру создания клиента от фикструы авторизации по серту"""
    #return DepartmentClient(client=private_auth_cert_client.client)
    return get_employees_cert_client(http_client=private_auth_cert_client.client)

class NewEmployee(BaseModel):
    response: CreateEmployeeResponseSchema

    @property
    def get_id_new_employee(self) -> str:
        id = self.response.id_new_employee
        return(id)

@pytest.fixture
def create_new_employee(employees_client: EmployeesClient, list_departments: Department) -> NewEmployee:
    request = CreateEmployeeRequestSchema(department_id=list_departments.get_department_id)
    response = employees_client.create_employee(request)
    # Т.к. в ответе просто приходится id нового департамента, то обернем его
    raw_data = json.loads(response.content)
    wrapped_data = {"id_new_employee": raw_data}  # оборачиваем массив в объект
    json_wrapped = json.dumps(wrapped_data)  # снова преобразуем в JSON‑строку
    response_data = CreateEmployeeResponseSchema.model_validate_json(json_wrapped)
    #return NewEmployee(response= response_data)
    employee = NewEmployee(response=response_data)
    #До yeld код выполняется перед тестом
    # Отдаём объект в тест (наш NewEmployee)
    yield employee

    #Всё, что после yield, выполнится после теста
    # --- TEARDOWN: удаляем ---
    delete_request = DeleteEmployeeRequestSchema(
        employee_id=employee.get_id_new_employee,
        ignore_warning=True
    )
    employees_client.delete_employee(delete_request)


class EmpoyeeInfo(BaseModel):
    response: GetEmployeeResponseSchema

    @property
    def get_id_authority(self) -> str:
        id = self.response.employee.employee_authority.id
        return(id)
    @property
    def get_lastname_authority(self) -> str:
        name = self.response.employee.last_name
        return(name)

@pytest.fixture
def get_empoyee_info(employees_client: EmployeesClient, create_new_employee: NewEmployee) -> EmpoyeeInfo:
        request = GetEmployeeRequestSchema(employee_id= create_new_employee.get_id_new_employee)
        response = employees_client.get_employee(request)
        response_data = GetEmployeeResponseSchema.model_validate_json(response.text)
        return EmpoyeeInfo(response= response_data)

@pytest.fixture
def delete_user(employees_cert_client: EmployeesClient, create_new_employee: NewEmployee):
        request = DeleteEmployeeRequestSchema(employee_id= create_new_employee.get_id_new_employee,
                                              ignore_warning= True)

        response = employees_cert_client.delete_employee(request)