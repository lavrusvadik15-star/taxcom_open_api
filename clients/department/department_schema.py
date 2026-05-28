from pydantic import BaseModel, ConfigDict


class DepartmentListSchema(BaseModel):
    """Схема данных в списке отеделений"""
    model_config = ConfigDict(populate_by_name=True)

    id: str
    name: str

class GetListDepartmentsResponseSchema(BaseModel):
    """Струкрута ответа на запрос списка отделов"""

    infos: list[DepartmentListSchema]