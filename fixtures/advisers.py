import pytest
import json
from pydantic import BaseModel

from clients.advisers.advisers_client import AdvisersClient, get_advisers_client
from clients.advisers.advisers_schema import AdvisersSchema, GetAdvisersResponseSchema
from fixtures.auth import CabinetSchema



class Advisers(BaseModel):
    response: GetAdvisersResponseSchema

    @property
    def get_advisers_id(self) -> int:
        advisers_id = self.response.advisers[0].id
        return (advisers_id)

@pytest.fixture
def advisers_client(auth_cabinet: CabinetSchema) -> AdvisersClient :
    """Создаем клиент для advissers от фикструы авторизации по кредам кабинета"""
    return get_advisers_client(auth_cabinet.credentials)

@pytest.fixture
def get_advisor(advisers_client: AdvisersClient) -> Advisers:
    #запрос
    response = advisers_client.get_advisers()
    #декодируем
    response_string = response.content.decode('utf-8')

    # тут возвращает массив, а не объект, потому преобразуем JSON‑массив в объект нашей схемы
    raw_data = json.loads(response_string)  # парсим JSON в Python‑структуру
    wrapped_data = {"advisers": raw_data}  # оборачиваем массив в объект
    json_wrapped = json.dumps(wrapped_data)  # снова преобразуем в JSON‑строку

    #преобразуем в объект по схеме
    response_data = GetAdvisersResponseSchema.model_validate_json(json_wrapped)
    return Advisers(response = response_data)