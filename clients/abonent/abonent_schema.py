from typing import Optional, Any

from pydantic import BaseModel, Field, ConfigDict
#from typing_inspection.typing_objects import alias


class GetAbonentRequest(BaseModel):
    """Структура запроса данных абонента"""
    model_config = ConfigDict(populate_by_name=True)

    abonent_id: str = Field(alias="AbonentId")

class AbonentSchema(BaseModel):
    """Модель абонента"""
    id: str
    inn: str
    kpp: str
    full_name: str = Field(alias="fullName")
    short_name: str = Field(alias="shortName")
    cabinet_name: str = Field(alias="cabinetName")
    is_public_cabinet_name: bool = Field(alias="isPublicCabinetName")
    cabinet_owner: Optional[str] = Field(alias="cabinetOwner")
    edx_client_id: str = Field(alias="edxClientId")
    is_test_abonent: bool = Field(alias="isTestAbonent")
    is_roaming_abonent: bool = Field(alias="isRoamingAbonent")
    is_demo_abonent: bool = Field(alias="isDemoAbonent")
    managed_by_partner_id: str = Field(alias="managedByPartnerId")

class GetAbonentResponseSchema(BaseModel):
    """ Структура ответа на запрос GetAbonent"""
    abonent : AbonentSchema

class GetAbonentRequisitesResponseSchema(BaseModel):
    """ Структура ответа на запрос GetAbonentRequisites"""
    model_config = ConfigDict(populate_by_name=True)

    inn: str
    name: str
    short_name: str = Field(alias="shortName")
    address: str
    kpp: str
    ogrn: str
    cabinet_name: str = Field(alias="cabinetName")
    is_public_cabinet_name: bool = Field(alias="isPublicCabinetName")
    edx_client_id: str = Field(alias="edxClientId")
    responsible_person_first_name: str = Field(alias="responsiblePersonFirstName")
    responsible_person_last_name: str = Field(alias="responsiblePersonLastName")
    responsible_person_patronymic: str = Field(alias="responsiblePersonPatronymic")


class AuthoritySchema(BaseModel):
    """Структура сущности прав пользователя"""
    model_config = ConfigDict(populate_by_name=True)

    id: int
    employee_id: str = Field(alias="employeeId")
    authority_confirm_method_id: int = Field(alias="authorityConfirmMethodId")
    warrant_signer_first_name: str = Field(alias="warrantSignerFirstName")
    warrant_signer_last_name: str = Field(alias="warrantSignerLastName")
    warrant_signer_middle_name: str = Field(alias="warrantSignerMiddleName")
    warrant_deal_date: str = Field(alias="warrantDealDate")
    warrant_reg_number: str = Field(alias="warrantRegNumber")
    warrant_internal_number: str = Field(alias="warrantInternalNumber")
    warrant_signer_data: str = Field(alias="warrantSignerData")
    warrant_internal_start_date: str = Field(alias="warrantInternalStartDate")
    warrant_internal_end_date: str = Field(alias="warrantInternalEndDate")
    storage_system_name: str = Field(alias="storageSystemName")
    additional_data: str = Field(alias="additionalData")


class EmployeeSchema(BaseModel):
    """Структура сущности Сотрудник"""
    model_config = ConfigDict(populate_by_name=True)

    id: str
    parent_id: str = Field(alias="parentId")
    abonent_id: str = Field(alias="abonentId")
    login: str
    password: str
    name: str
    first_name: str = Field(alias="firstName")
    last_name: str = Field(alias="lastName")
    patronymic: str
    email: str
    position: str
    permissions: Optional[Any]
    snils: str
    department_name: str = Field(alias="departmentName")
    is_removed: bool = Field(alias="isRemoved")
    created: str = Field(alias="created")  #  может datetime тип ??
    employee_authority: AuthoritySchema = Field(alias="employeeAuthority")


class DepartmentSchema(BaseModel):
    """Структура сущности Подраздление"""
    model_config = ConfigDict(populate_by_name=True)

    id: str
    name: str
    parent_department_id: str = Field(alias="parentDepartmentId")
    kpp: str
    address: str
    show_to_contractors: bool = Field(alias="showToContractors")
    replace_to_department_if_same_address: bool = Field(alias="replaceToDepartmentIfSameAddress")
    replace_to_department_if_same_kpp: bool = Field(alias="replaceToDepartmentIfSameKpp")
    employee_list: Optional[list[EmployeeSchema]] = Field(alias="employeeList")
    isRemoved: bool = Field(alias="isRemoved")


class AvailableDepartmentsResponseSchema(BaseModel):
    """Стуктура ответа на запрос список доступных подразделений"""
    model_config = ConfigDict(populate_by_name=True)

    items: list[DepartmentSchema]

class GetMobileQRResponseSchema(BaseModel):
    """Стурктра ответа получения QR кода в мобильном приложении"""
    model_config = ConfigDict(populate_by_name=True)

    qr: str

class GetAutopilotStatusResponseSchema(BaseModel):
    """Структура ответа статус подключения сдк - ассистента"""
    model_config = ConfigDict(populate_by_name=True)

    is_on: bool = Field(alias="isOn")
