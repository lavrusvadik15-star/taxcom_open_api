from pathlib import Path

import pytest
from cryptography.x509 import load_der_x509_certificate, load_pem_x509_certificate
from cryptography.hazmat.primitives.serialization import Encoding, PublicFormat

# @pytest.fixture
# def certificate_base64_str() -> str:
#     # Читаем сразу готовую Base64-строку из файла, который создали выше
#     path = r"C:\Pycharm\taxcom\testdata\cert_base64_string.txt"
#     return Path(path).read_text(encoding='ascii').strip()



