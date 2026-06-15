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

class EmployeeAuthoritySchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: int = Field(alias="id")
    employee_id: str = Field(alias="employeeId")
    authority_confirm_method_id: Optional[int] = Field(default=None, alias="authorityConfirmMethodId")
    warrant_signer_first_name: Optional[str] = Field(default=None, alias="warrantSignerFirstName")
    warrant_signer_last_name: Optional[str] = Field(default=None, alias="warrantSignerLastName")
    warrant_signer_middle_name: Optional[str] = Field(default=None, alias="warrantSignerMiddleName")
    warrant_deal_date: Optional[str] = Field(default=None, alias="warrantDealDate")
    warrant_reg_number: Optional[str] = Field(default=None, alias="warrantRegNumber")
    warrant_internal_number: Optional[str] = Field(default=None, alias="warrantInternalNumber")
    warrant_signer_data: Optional[str] = Field(default=None, alias="warrantSignerData")
    warrant_internal_start_date: Optional[str] = Field(default=None, alias="warrantInternalStartDate")
    warrant_internal_end_date: Optional[str] = Field(default=None, alias="warrantInternalEndDate")
    storage_system_name: Optional[str] = Field(default=None, alias="storageSystemName")
    additional_data: Optional[str] = Field(default=None, alias="additionalData")

class CreateEmployeeRequestSchema(BaseModel):
    """Схема создания нового пользователя в системе"""
    model_config = ConfigDict(populate_by_name=True)

    email: Optional[str] = Field(default=None, alias="email")
    last_name: Optional[str] = Field(default=None, alias="lastName")
    first_name: Optional[str] = Field(default=None, alias="firstName")
    patronymic: Optional[str] = Field(default=None, alias="patronymic")
    position: Optional[str] = Field(default=None, alias="position")
    permissions: Optional[str] = Field(default=None, alias="permissions")
    department_id: Optional[str] = Field(default=None, alias="departmentId")
    access_allowed_departments: list[str] = Field(default_factory=list, alias="accessAllowedDepartments")
    signer_auth_areas_id: Optional[int] = Field(default=None, alias="signerAuthAreasId")
    signer_status_id: Optional[int] = Field(default=None, alias="signerStatusId")
    basis_authority: Optional[str] = Field(default=None, alias="basisAuthority")
    change_password_url: Optional[str] = Field(default=None, alias="changePasswordUrl")
    employee_authority: Optional[EmployeeAuthoritySchema] = Field(default=None, alias="employeeAuthority")