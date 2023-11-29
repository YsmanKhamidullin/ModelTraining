# jp_ocr.py

from manga_ocr import MangaOcr


def extract_text_from_image(image_path):
    mocr = MangaOcr()
    text = mocr(image_path)
    return text
