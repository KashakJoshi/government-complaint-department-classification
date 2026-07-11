import pytesseract
from PIL import Image

from predict import predict_department


def image_to_text(image_path):

    image = Image.open(image_path)

    text = pytesseract.image_to_string(
        image,
        lang="eng"
    )

    return text


def process_image(image_path):

    text = image_to_text(image_path)

    result = predict_department(text)

    return {
        "text": text,
        "prediction": result
    }