# utils/crypto_pro.py
import base64
import os
import subprocess
import tempfile
from pathlib import Path

def safe_b64_decode(data: str) -> bytes:
    if not isinstance(data, str):
        raise TypeError("Base64-данные должны быть строкой")
    clean = "".join(data.split())
    if len(clean) == 0:
        raise ValueError("Base64-строка пустая после очистки")
    return base64.b64decode(clean, validate=True)


def decrypt_cms_with_csptest(base64_data: str, thumbprint: str, output_path: str, cert_store: str = "MY"):
    cms_bytes = safe_b64_decode(base64_data)

    with tempfile.NamedTemporaryFile(delete=False, suffix=".cms") as tmp:
        tmp.write(cms_bytes)
        enc_path = tmp.name

    candidates = [
        r"C:\Program Files\Crypto Pro\CSP\csptest.exe",
        r"C:\Program Files (x86)\Crypto Pro\CSP\csptest.exe"
    ]
    csptest_path = None
    for p in candidates:
        if os.path.isfile(p):
            csptest_path = p
            break
    if not csptest_path:
        os.unlink(enc_path)
        raise FileNotFoundError(
            "csptest.exe не найден. Проверьте установку КриптоПро."
        )

    try:
        cmd = [
            csptest_path,
            "-lowenc",
            "-decrypt",
            f"-{cert_store}", thumbprint,
            "-in", enc_path,
            "-out", output_path
        ]

        res = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace"
        )
        if res.returncode != 0:
            raise RuntimeError(
                f"Ошибка csptest: {res.stderr.strip() or res.stdout}"
            )
    finally:
        if os.path.exists(enc_path):
            os.unlink(enc_path)


def decrypt_and_get_bytes(base64_data: str, thumbprint: str, cert_store: str = "MY") -> bytes:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".bin") as tmp_out:
        out_path = tmp_out.name

    try:
        decrypt_cms_with_csptest(base64_data, thumbprint, out_path, cert_store)
        with open(out_path, "rb") as f:
            return f.read()
    finally:
        if os.path.exists(out_path):
            os.unlink(out_path)
