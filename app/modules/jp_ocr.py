# jp_ocr.py
from typing import Annotated

from fastapi import File
from manga_ocr import MangaOcr


def extract_text_from_image(image: Annotated[bytes, File()]):
    temp_image_path = "temp_image.png"
    with open(temp_image_path, "wb") as temp_image:
        temp_image.write(image)
    return extract_text_from_image_path(temp_image_path)


def extract_text_from_image_path(image_path):
    mocr = MangaOcr()
    text = mocr(image_path)
    return text
