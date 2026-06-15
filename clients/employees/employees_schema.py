from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class Employee(BaseModel):
    id: str = Field(alias="id")
    parent_id: Optional[str] = Field(default=None, alias="parentId")
    abonent_id: Optional[str] = Field(default=None, alias="abonentId")
    login: str = Field(alias="login")
    name: Optional[str] = Field(default=None, alias="name")
    first_name: Optional[str] = Field(default=None, alias="firstName")
    last_name: Optional[str] = Field(default=None, alias="lastName")
    patronymic: Optional[str] = Field(default=None, alias="patronymic")
    email: Optional[str] = Field(default=None, alias="email")
    position: Optional[str] = Field(default=None, alias="position")
    permissions: Optional[str] = Field(default=None, alias="permissions")
    department_name: Optional[str] = Field(default=None, alias="departmentName")

class GetListEmployeesResponseSchema(BaseModel):
    """Схема ответа на запрос списка сотрудников"""
    model_config = ConfigDict(populate_by_name=True)

    employees: list[Employee]