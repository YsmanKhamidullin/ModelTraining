# fastapi_app.py

from typing import Annotated
from fastapi import FastAPI, File
from ocr.jp_ocr import extract_text_from_image

app = FastAPI()


@app.post("/ocr_image/")
async def ocr_image(file: Annotated[bytes, File()]):
    result = extract_text_from_image(file)
    return {"text": result}
