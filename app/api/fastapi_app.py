from typing import Annotated
from fastapi import FastAPI, File
from app.modules import jp_ocr

app = FastAPI()


@app.post("/ocr_image/")
async def ocr_image(file: Annotated[bytes, File()]):
    result = jp_ocr.extract_text_from_image(file)
    return {"text": result}
