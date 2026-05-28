from pydantic import BaseModel, ConfigDict, Field


class BannersSchema(BaseModel):
    """Схема баннера"""
    model_config = ConfigDict(populate_by_name=True)

    priority: int
    content: str
    url: str
    alt_text: str = Field(alias="altText")



class GetBannersResponseSchema(BaseModel):
    """Схема ответа на запрос получения баннеров"""

    banners: list[BannersSchema]