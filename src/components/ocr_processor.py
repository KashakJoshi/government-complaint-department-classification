import easyocr

from src.predict import predict_department


# =========================
# Load EasyOCR Model
# =========================

reader = easyocr.Reader(
    ['hi', 'en'],
    gpu=False
)


# =========================
# Image To Text
# =========================

def image_to_text(image_path):

    results = reader.readtext(
        image_path
    )

    text_list = []

    for result in results:
        text_list.append(result[1])

    text = " ".join(text_list)

    return text.strip()


# =========================
# Complete OCR Pipeline
# =========================

def process_image(image_path):

    try:

        text = image_to_text(
            image_path
        )

        prediction = predict_department(
            text
        )

        return {
            "text": text,
            "prediction": prediction
        }


    except Exception as e:

        return {
            "error": f"OCR processing failed: {str(e)}"
        }