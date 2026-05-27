from httpx import Client


#Тут мы создадим публичный HTTP клиент с необходимыми параметрами,
# которые будут использоваться во всех публичных апи (без авторизации которые)
def get_public_http_client() -> Client:
    """
    Создает и возвращает новый экземляр клиента для работы с публичным API
    :return: Готовый объект httpx.Client
    """
    return Client(timeout=100,
                  #proxy=None,  # Отключаем использование системного прокси
                  #base_url="https://stage-newfiler-api.taxcom.ru"
                  base_url="http://stage-web:57000"
                )