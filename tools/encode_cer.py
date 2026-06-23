import base64
from pathlib import Path

# Исходный файл (тот самый DER-сертификат, который у тебя был изначально)
cert_path = r"C:\Pycharm\taxcom\testdata\Soloviev_test.cer"
# Сюда сохраним готовую строку (для проверки или если захочешь положить в конфиг)
output_txt = r"C:\Pycharm\taxcom\testdata\cert_base64_string.txt"

# Читаем бинарные данные сертификата
cert_bytes = Path(cert_path).read_bytes()

# Кодируем в Base64 (это то, что ждёт сервер)
base64_bytes = base64.b64encode(cert_bytes)
base64_string = base64_bytes.decode('ascii')

# Сохраняем в файл, чтобы видеть длину (она будет большой, как на фронте)
Path(output_txt).write_text(base64_string, encoding='ascii')
