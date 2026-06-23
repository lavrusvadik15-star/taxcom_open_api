import httpx

def private_client_with_cert(token: str) -> httpx.Client:
    """
    Создаёт httpx.Client с заголовком Authorization.
    Принимает ТОЛЬКО токен (без префикса Bearer — добавим здесь).
    Никакой логики логина, никаких файлов, никаких фикстур.
    """
    return httpx.Client(
        timeout=100,
        base_url="http://stage-web:57000",
        headers={"Authorization": f"Bearer {token}"},
    )
