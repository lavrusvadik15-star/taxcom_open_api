from typing import Optional, Any

from pydantic import BaseModel, Field, ConfigDict, EmailStr

from tools.fakers import fake


class AdvisersSubscriptionSchema(BaseModel):
    """Структура подписанного адвайзера"""
    model_config = ConfigDict(populate_by_name=True)

    adviser_id: int = Field(alias="adviserId")
    abonent_id: str = Field(alias="abonentId")
    email: EmailStr

class AdvisersSchema(BaseModel):
    """Структура ответа на получение списка адвайзеров"""
    model_config = ConfigDict(populate_by_name=True)

    id: int
    title: str
    text: str
    cookie_postfix: str
    is_subscribable: bool = Field(alias="isSubscribable")
    priority: int
    start_showing_datetime: Optional[Any] = Field(alias="startShowingDatetime")
    end_showing_datetime: Optional[Any] = Field(alias="endShowingDatetime")

class GetAdvisersResponseSchema(BaseModel):
    """Структура ответа на получение списка адвайзеров"""
    model_config = ConfigDict(populate_by_name=True)

    advisers : list[AdvisersSchema]

class SubscribeAdvisersRequestSchema(BaseModel):
    """структура Запроса подписки на адвайзер"""
    model_config = ConfigDict(populate_by_name=True)

    adviser_id: int = Field(alias="adviserId")
    email: str = Field(default_factory=fake.email)

class UnsubscribeAdvisersRequestSchema(BaseModel):
    """структураЗакрытие запроса отписки от адвазера"""
    model_config = ConfigDict(populate_by_name=True)

    #Тут запрос не валидируется никак, можно добавить фикстуру подписания, если надо, но можно и любое число для отписки вставлять
    adviser_id: int = Field(alias="adviserId", default_factory=fake.integer)

class GetAdviserSubscriptionResponseSchema(BaseModel):
    """Структура ответа на запрос списка подписанных адвазеров"""

    adviser: list[AdvisersSubscriptionSchema]

