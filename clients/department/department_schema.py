from datetime import datetime
from enum import Enum
from typing import Optional, List

from pydantic import BaseModel, ConfigDict, Field


class DepartmentListSchema(BaseModel):
    """Схема данных в списке отеделений"""
    model_config = ConfigDict(populate_by_name=True)

    id: str
    name: str

class GetListDepartmentsResponseSchema(BaseModel):
    """Струкрута ответа на запрос списка отделов"""

    infos: list[DepartmentListSchema]

#С Enum при парсинге ответа API Pydantic проверит, что значение есть в списке
class EmployeePermission(str, Enum):
    """Структура прав сотрудника (Enum позволяет переменной принимать только заранее заданный список значений) """
    None_ = "None" # добавил _ чтобы не было конфликт с Python именами
    Administrator = "Administrator"
    ManageDepartment = "ManageDepartment"
    InheritToChild = "InheritToChild"
    CreateDocument = "CreateDocument"
    ApproveDocument = "ApproveDocument"
    SignDocument = "SignDocument"
    SendDocumentToSign = "SendDocumentToSign"
    MoveDocument = "MoveDocument"
    ImportCreateDocument = "ImportCreateDocument"
    CanAccessToContacts = "CanAccessToContacts"
    SendDocument = "SendDocument"
    EditRequisites = "EditRequisites"
    EnableLoginByCertificate = "EnableLoginByCertificate"
    ManageEmployees = "ManageEmployees"
    ManageWarrants = "ManageWarrants"
    ManageCabinets = "ManageCabinets"
    ManageSettings = "ManageSettings"
    TaxcomDocuments = "TaxcomDocuments"
    All = "All"

class EmployeeAuthorityDetails(BaseModel):
    """Структура полномочий сотрудника"""
    model_config = ConfigDict(populate_by_name=True)

    id: int
    employee_id: str = Field(alias="employeeId")
    authority_confirm_method_id: Optional[int] = Field(default=None, alias="authorityConfirmMethodId")
    warrant_signer_first_name: Optional[str] = Field(default=None, alias="warrantSignerFirstName")
    warrant_signer_last_name: Optional[str] = Field(default=None, alias="warrantSignerLastName")
    warrant_signer_middle_name: Optional[str] = Field(default=None, alias="warrantSignerMiddleName")
    warrant_deal_date: Optional[datetime] = Field(default=None, alias="warrantDealDate")
    warrant_reg_number: Optional[str] = Field(default=None, alias="warrantRegNumber")
    warrant_internal_number: Optional[str] = Field(default=None, alias="warrantInternalNumber")
    warrant_signer_data: Optional[str] = Field(default=None, alias="warrantSignerData")
    warrant_internal_start_date: Optional[datetime] = Field(default=None, alias="warrantInternalStartDate")
    warrant_internal_end_date: Optional[datetime] = Field(default=None, alias="warrantInternalEndDate")
    storage_system_name: Optional[str] = Field(default=None, alias="storageSystemName")
    additional_data: Optional[str] = Field(default=None, alias="additionalData")

class Employee(BaseModel):
    """Структура данных о сотруднике"""
    id: str
    parent_id: str = Field(alias="parentId")
    abonent_id: str = Field(alias="abonentId")
    login: Optional[str] = Field(default=None, alias="login")
    password: Optional[str] = Field(default=None, alias="password")
    name: Optional[str] = Field(default=None, alias="name")
    first_name: Optional[str] = Field(default=None, alias="firstName")
    last_name: Optional[str] = Field(default=None, alias="lastName")
    patronymic: Optional[str] = Field(default=None, alias="patronymic")
    email: Optional[str] = Field(default=None, alias="email")
    position: Optional[str] = Field(default=None, alias="position")
    permissions: EmployeePermission = Field(alias="permissions")
    snils: Optional[str] = Field(default=None, alias="snils")
    department_name: Optional[str] = Field(default=None, alias="departmentName")
    is_removed: bool = Field(alias="isRemoved")
    created: datetime = Field(alias="created")
    employee_authority: Optional[EmployeeAuthorityDetails] = Field(default=None, alias="employeeAuthority")

class DepartmentNode(BaseModel):
    """Модель для одного узла дерева"""
    id: str
    name: str
    parent_department_id: Optional[str] = Field(default=None, alias="parentDepartmentId")
    kpp: Optional[str] = Field(default=None)
    address: Optional[str] = Field(default=None, alias="address")
    show_to_contractors: bool = Field(alias="showToContractors")
    replace_to_department_if_same_address: bool = Field(alias="replaceToDepartmentIfSameAddress")
    replace_to_department_if_same_kpp: bool = Field(alias="replaceToDepartmentIfSameKpp")
    employee_list: Optional[list[Employee]] = Field(default=None, alias="employeeList")


class DepartmentNodeWithChildren(BaseModel):
    """Стурктра ответа для дерева подразделений
    Тут задана рекурсия, т.к. `children' может быть бесконечным"""
    model_config = ConfigDict(populate_by_name=True)

    department: DepartmentNode
    #Кавычки обязательны: так Pydantic понимает, что тип будет определён позже. Это единственный способ сделать рекурсивную модель.
    children: Optional[list["DepartmentNodeWithChildren"]] = Field(default=None)


class GetDepartmentTreeResponseSchema(BaseModel):
    """Схема ответа на запрос дерева подразделений."""
    department: DepartmentNode
    children: Optional[list[DepartmentNodeWithChildren]] = Field(default=None)

