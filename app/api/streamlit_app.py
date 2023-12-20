import streamlit as st
from app.modules import jp_ocr


def open_image():
    upload_file = st.file_uploader(label="Load file")

    if upload_file is not None:
        try:
            image_data = upload_file.getvalue()
            st.image(image_data)
            return image_data
        except Exception as e:
            st.error(f"Error: {str(e)}")
            return None
    else:
        return None


def run_app():
    img_data = open_image()

    if img_data is not None:
        try:
            st.text(f"Processing...")
            extracted_text = jp_ocr.extract_text_from_image(img_data)
            st.text(f"Extracted Text: {extracted_text}")
        except Exception as e:
            st.error(f"Error: {str(e)}")


if __name__ == '__main__':
    run_app()
