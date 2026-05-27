from typing import Optional, Any

from pydantic import BaseModel, Field, ConfigDict

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