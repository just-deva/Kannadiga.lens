"""Dependency-free local API for kannadiga.lens.

Live recognition uses a locally installed Tesseract with Kannada data. The UI may
be run in demo mode when that optional dependency is not present.
"""
from __future__ import annotations

import base64
import binascii
import json
import os
import re
import shutil
import subprocess
import tempfile
from http import HTTPStatus
from http.server import HTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parent
MIME = {
    ".html": "text/html; charset=utf-8",
    ".css": "text/css; charset=utf-8",
    ".js": "text/javascript; charset=utf-8",
}


def gloss(text: str) -> str:
    dictionary = {
        "ನಮಸ್ಕಾರ": "Hello",
        "ಧನ್ಯವಾದ": "Thank you",
        "ಬೆಂಗಳೂರು": "Bengaluru",
        "ಪುಸ್ತಕ": "Book",
        "ಸ್ವಾಗತ": "Welcome",
        "ಕನ್ನಡ": "Kannada",
        "ಶಾಲೆ": "School",
    }
    found = [english for kannada, english in dictionary.items() if kannada in text]
    return (
        " · ".join(found)
        if found
        else "Kannada text digitized and ready to search"
    )


class App(SimpleHTTPRequestHandler):

    def translate_path(self, path: str) -> str:
        requested = urlparse(path).path
        if requested == "/":
            requested = "/index.html"
        return str(ROOT / requested.lstrip("/"))

    def end_headers(self):
        self.send_header("Cache-Control", "no-store")
        super().end_headers()

    def guess_type(self, path):
        return MIME.get(Path(path).suffix, super().guess_type(path))

    def do_POST(self):
        if urlparse(self.path).path != "/api/extract":
            self.send_error(HTTPStatus.NOT_FOUND)
            return
        try:
            length = int(self.headers.get("Content-Length", "0"))
            payload = json.loads(self.rfile.read(length))
            raw = payload.get("image", "")
            if not raw.startswith("data:image/") or "," not in raw:
                raise ValueError("Please choose an image file.")
            image = base64.b64decode(raw.split(",", 1)[1], validate=True)
            executable = shutil.which("tesseract")
            if not executable:
                self.reply(
                    {
                        "ok": False,
                        "error": (
                            "Live OCR needs Tesseract with Kannada language"
                            " data. Try the sample while it is being installed."
                        ),
                    },
                    HTTPStatus.SERVICE_UNAVAILABLE,
                )
                return
            suffix = (
                "."
                + raw.split(";", 1)[0].split("/", 1)[-1].replace("jpeg", "jpg")
            )
            with tempfile.NamedTemporaryFile(
                suffix=suffix, delete=False
            ) as source:
                source.write(image)
                source_path = source.name
            result = subprocess.run(
                [
                    executable,
                    source_path,
                    "stdout",
                    "-l",
                    "kan+eng",
                    "--psm",
                    "6",
                ],
                capture_output=True,
                text=True,
                timeout=60,
            )
            Path(source_path).unlink(missing_ok=True)
            if result.returncode:
                raise RuntimeError(
                    "Kannada OCR could not run. Confirm that kan.traineddata is"
                    " installed."
                )
            text = re.sub(r"[ \t]+", " ", result.stdout).strip()
            self.reply(
                {
                    "ok": True,
                    "text": text or "ಯಾವುದೇ ಪಠ್ಯ ಪತ್ತೆಯಾಗಲಿಲ್ಲ",
                    "translation": gloss(text),
                    "source": "Live OCR",
                }
            )
        except (ValueError, binascii.Error) as error:
            self.reply(
                {"ok": False, "error": str(error)}, HTTPStatus.BAD_REQUEST
            )
        except Exception as error:
            self.reply(
                {"ok": False, "error": str(error)},
                HTTPStatus.INTERNAL_SERVER_ERROR,
            )

    def reply(self, body, status=HTTPStatus.OK):
        encoded = json.dumps(body, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(encoded)))
        self.end_headers()
        self.wfile.write(encoded)


if __name__ == "__main__":
    PORT = int(os.environ.get("PORT", 4173))
    server_address = ("0.0.0.0", PORT)

    httpd = HTTPServer(server_address, App)

    print(f"kannadiga.lens server running on port {PORT}...")
    httpd.serve_forever()
