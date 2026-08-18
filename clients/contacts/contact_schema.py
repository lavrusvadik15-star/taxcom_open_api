from datetime import datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class GetContactListRequestSchema(BaseModel):
    """Схема запроса получения контактов"""
    model_config = ConfigDict(populate_by_name=True)

    search_text: str = Field(alias="searchText", default="")
    items_per_page: int = Field(alias="itemsPerPage", default=10)
    page: int = Field(default=1)
    status_filters: list[str] = Field(default=[], alias="statusFilters")
    self_include: bool = Field(alias="selfInclude", default=False)
    include_epd_recipients: bool = Field(alias="includeEpdRecipients", default=False)


class ContactPairStatus(str, Enum):
    """Статус пары контактов"""
    SENT = "Sent"
    ACCEPTED = "Accepted"
    REJECTED = "Rejected"
    UNKNOWN = "Unknown"


class ContactItemSchema(BaseModel):
    """Схема контакта в ответе"""
    model_config = ConfigDict(populate_by_name=True)

    contact_pair_id: str = Field(alias="contactPairId")
    contact_abonent_id: Optional[str] = Field(alias="contactAbonentId")
    nickname: str
    name: Optional[str]
    short_name: Optional[str] = Field(alias="shortName")
    inn: str
    kpp: Optional[str]
    email: Optional[str]
    cabinet_name: Optional[str] = Field(alias="cabinetName")
    is_public_cabinet_name: bool = Field(alias="isPublicCabinetName")
    edx_client_id: str = Field(alias="edxClientId")
    operator_name: str = Field(alias="operatorName")
    changed: Optional[str]
    is_test_abonent: bool = Field(alias="isTestAbonent")
    is_roaming: bool = Field(alias="isRoaming")
    last_login_date: Optional[str] = Field(default=None, alias="lastLoginDate")
    is_active: Optional[bool] = Field(alias="isActive")
    is_added_contact: bool = Field(alias="isAddedContact")
    abonent_pays_for_income: bool = Field(alias="abonentPaysForIncome")
    contact_pair_status: ContactPairStatus = Field(alias="contactPairStatus")
    invitation_message: Optional[str] = Field(default=None, alias="invitationMessage")
    comment: Optional[str] = None
    address: Optional[str] = None
    contracts: Optional[list[str]] = Field(default_factory=list)
    custom_address: Optional[str] = Field(default=None, alias="customAddress")


class GetContactListResponseSchema(BaseModel):
    """Схема ответа получения контактов"""
    model_config = ConfigDict(populate_by_name=True)

    total_items: int = Field(alias="totalItems")
    page: int
    contacts: list[ContactItemSchema]


class ContactLowSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: str
    name: str

class GetContactListAsDictionaryItemsResponseSchema(BaseModel):
    """Схема ответа на запрос контактов в простом виде"""
    model_config = ConfigDict(populate_by_name=True)

    contact_low: list[ContactLowSchema]