from pydantic import BaseModel, Field, ConfigDict
from typing import List, Optional
from datetime import datetime
from enum import Enum


class DocumentType(str, Enum):
    """Тип документа"""
    UNKNOWN = "Unknown"
    STATEMENT = "Statement"
    OFFSETTING_STATEMENT = "OffsettingStatement"
    RECONCILIATION_STATEMENT = "ReconciliationStatement"
    SHEET = "Sheet"
    GUARANTEE_LETTER = "GuaranteeLetter"
    CONTRACT = "Contract"
    ADDITIONAL_AGREEMENT = "AdditionalAgreement"
    KS2 = "KS2"
    KS3 = "KS3"
    KS11 = "KS11"
    REPORT = "Report"
    OTHER = "Other"
    PAYMENT_ORDER = "PaymentOrder"
    STATEMENT_APPENDIX = "StatementAppendix"
    EDO_AGREEMENT = "EDOAgreement"
    SPECIFICATION = "Specification"
    ACCOUNT = "Account"
    CONSIGNMENT = "Consignment"
    NOTIFICATION = "Notification"
    AGENT_REPORT = "AgentReport"


class CreateDocumentRequestSchema(BaseModel):
    """Схема запроса создания документа"""
    model_config = ConfigDict(populate_by_name=True)

    # Обязательные поля
    document_type: DocumentType = Field(alias="documentType")
    document_number: str = Field(alias="documentNumber")
    document_sum: str = Field(alias="documentSum")
    document_date: datetime = Field(alias="documentDate")
    receiver_abonent_id: str = Field(alias="receiverAbonentId")
    resign_required: bool = Field(alias="resignRequired")
    attachment_file_name: str = Field(alias="attachmentFileName")
    attachment_file_content: str = Field(alias="attachmentFileContent")

    # Необязательные поля с дефолтами
    sender_contact_info_department_id: Optional[str] = Field(default=None, alias="senderContactInfoDepartmentId")
    sender_contact_info_department_name: str = Field(default="", alias="senderContactInfoDepartmentName")
    sender_contact_info_full_name: str = Field(default="", alias="senderContactInfoFullName")
    sender_contact_info: str = Field(default="", alias="senderContactInfo")
    receiver_contact_info_department_id: Optional[str] = Field(default=None, alias="receiverContactInfoDepartmentId")
    receiver_contact_info_department_name: str = Field(default="", alias="receiverContactInfoDepartmentName")
    receiver_contact_info_full_name: str = Field(default="", alias="receiverContactInfoFullName")
    receiver_contact_info: str = Field(default="", alias="receiverContactInfo")
    kpp_receiver: Optional[str] = Field(default=None, alias="kppReceiver")
    agreement: str = Field(default="")
    document_additional_file_name: Optional[str] = Field(default=None, alias="documentAdditionalFileName")
    document_additional_file_content: str = Field(default="", alias="documentAdditionalFileContent")
    link_package_chain_ids: List[str] = Field(default_factory=list, alias="linkPackageChainIds")
    deal_number: str = Field(default="", alias="dealNumber")
    subject: str = Field(default="")
    comment: str = Field(default="")
    warrant_id: Optional[int] = Field(default=None, alias="warrantId")
    group_id: Optional[int] = Field(default=None, alias="groupId")