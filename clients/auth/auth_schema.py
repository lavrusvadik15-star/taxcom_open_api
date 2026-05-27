from typing import Optional

from pydantic import BaseModel, ConfigDict, Field

from clients.abonent.abonent_schema import AbonentSchema
from tools.fakers import fake


class LoginRequestSchema(BaseModel):
    """Структура запроса на логин по логину и паролю"""
    model_config = ConfigDict(populate_by_name=True)

    login: str = Field(default_factory=fake.word)
    password: str = Field(default_factory=fake.password)
    abonent_id: str = Field(alias="abonentId", default_factory=lambda: None)
    two_step_auth_code: str = Field(alias="twoStepAuthCode", default_factory=fake.word)

# class AbonentSchema(BaseModel):
#     """Модель абонента"""
#     id: str
#     inn: str
#     kpp: str
#     fullName: str
#     shortName: str
#     cabinetName: str
#     isPublicCabinetName: bool
#     cabinetOwner: str
#     edxClientId: str
#     isTestAbonent: bool
#     isRoamingAbonent: bool
#     isDemoAbonent: bool
#     managedByPartnerId: str

class EmployeeInfoSchema(BaseModel):
    """Модель информации о сотруднике"""
    id: str
    firstName: str
    lastName: str
    patronymic: str | None = None
    permissions: str

class LoginResponseSchema(BaseModel):
    """
    Структура ответа на логин по логину и паролю
    """
    model_config = ConfigDict(populate_by_name=True)

    login: Optional[str]
    result: str
    abonents: list[AbonentSchema]
    token: Optional[str]
    error_message: Optional[str] = Field(default=None, alias="errorMessage")
    employeeInfo: Optional[EmployeeInfoSchema]
    default_mchd_warrant_id: Optional[int] = Field(alias="defaultMchdWarrantId")
    is_required_mchd: bool = Field(alias="isRequiredMchd")

class LoginCertificateRequestSchema(BaseModel):
    """
    Стуктура запроса для авторизации с помощью сертификата
    """
    model_config = ConfigDict(populate_by_name=True)

    is_cloud: Optional[bool] = Field(alias="isCloud",default=None)
    certificate_public_key: str = Field(alias="certificatePublicKey")
    abonent_id: Optional[str] = Field(alias="abonentId",default=None)
    is_cert_new_qes: Optional[bool] = Field(alias="isCertNewQES", default=True)
    email: Optional[str] = Field(default=None)