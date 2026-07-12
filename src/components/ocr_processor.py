import pytesseract
from PIL import Image

from src.predict import predict_department

def image_to_text(image_path):

    try:

        image = Image.open(image_path)

        text = pytesseract.image_to_string(
            image,
            lang="eng"
        )

        if not text.strip():
            raise ValueError(
                "No text detected from image"
            )

        return text


    except Exception as e:

        raise Exception(
            f"OCR processing failed: {str(e)}"
        )



def process_image(image_path):

    try:

        text = image_to_text(
            image_path
        )

        result = predict_department(
            text
        )

        return {
            "text": text,
            "prediction": result
        }


    except Exception as e:

        return {
            "error": str(e)
        }