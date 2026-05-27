from typing import Optional, Any

from pydantic import BaseModel, Field, ConfigDict

from tools.fakers import fake


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