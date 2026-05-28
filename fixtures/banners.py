import pytest

from clients.banners.banners_client import BannersClient, get_banners_client
from fixtures.auth import CabinetSchema


@pytest.fixture
def banners_client(auth_cabinet: CabinetSchema) -> BannersClient:
    """Фикстура для получения клиента баннеров"""
    return get_banners_client(auth_cabinet.credentials)