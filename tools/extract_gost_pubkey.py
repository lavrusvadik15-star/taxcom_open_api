import base64
from pathlib import Path
from asn1crypto import x509, keys

cert_path = r"C:\Pycharm\taxcom\testdata\Soloviev_test.cer"
key_path = r"C:\Pycharm\taxcom\testdata\public_key.pem"

# 1. Читаем сертификат (DER, ГОСТ — asn1crypto просто парсит структуру)
cert = x509.Certificate.load(Path(cert_path).read_bytes())
pk: keys.PublicKeyInfo = cert.public_key

# 2. Получаем сырые байты публичного ключа (SubjectPublicKeyInfo)
raw_key_bytes = pk.dump()  # это bytes ASN.1 структуры

# 3. Сами кодируем в base64 (как это делает openssl)
base64_bytes = base64.b64encode(raw_key_bytes)
base64_string = base64_bytes.decode('ascii')  # base64 всегда ASCII

# 4. Формируем PEM-файл вручную (добавляем заголовки и переносы строк каждые 64 символа)
# asn1crypto dump() не делает переносы, а PEM требует их каждые 64 символа
pem_lines = [base64_string[i:i+64] for i in range(0, len(base64_string), 64)]
pem_content = (
    "-----BEGIN PUBLIC KEY-----\n" +
    "\n".join(pem_lines) +
    "\n-----END PUBLIC KEY-----"
)

Path(key_path).write_text(pem_content, encoding="ascii")
print(f"Готово: публичный ключ сохранён в {key_path}")
