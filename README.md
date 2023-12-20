# Translating text from screen to screen

[//]: # (### What and Why)

[//]: # ()

[//]: # (This project is for translating the text in your screen.)

### Getting start

Streamlit app:

```
git clone https://github.com/YsmanKhamidullin/ModelTraining.git
cd ModelTraining
python -m streamlit run .\app\api\streamlit_app.py
```
Open in browser: http://localhost:8501/

FastApi app:

```
git clone https://github.com/YsmanKhamidullin/ModelTraining.git
cd ModelTraining
uvicorn app.api.fastapi_app:app --reload 
```
Open in browser: http://127.0.0.1:8000/docs#/

### Current Implementation

> Get jp text from image

### Misc info

* > Maintainer
  [Ysman Khamidullin](https://github.com/YsmanKhamidullin)

# Model Source

[HuggingFace](https://huggingface.co/kha-white/manga-ocr-base), [GitHub](https://github.com/kha-white/manga-ocr)