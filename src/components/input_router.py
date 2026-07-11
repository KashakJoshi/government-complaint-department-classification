from src.predict import predict_department
from src.components.ocr_processor import process_image
from src.components.audio_processor import process_audio


def process_input(input_type, data):
    """
    Main Input Router

    input_type:
        text
        image
        audio

    data:
        text  -> complaint text
        image -> image path
        audio -> audio path
    """


    # =====================
    # TEXT INPUT
    # =====================
    if input_type == "text":

        result = predict_department(data)

        return {
            "input_type": "text",
            "complaint": data,
            "prediction": result
        }


    # =====================
    # IMAGE INPUT
    # =====================
    elif input_type == "image":

        result = process_image(data)

        return {
            "input_type": "image",
            "file": data,
            "prediction": result
        }


    # =====================
    # AUDIO INPUT
    # =====================
    elif input_type == "audio":

        result = process_audio(data)

        return {
            "input_type": "audio",
            "prediction": result
        }


    # =====================
    # INVALID INPUT
    # =====================
    else:

        return {
            "error": "Invalid input type. Use text/image/audio"
        }



# =====================
# LOCAL TEST
# =====================
if __name__ == "__main__":

    complaint = "मेरे गांव की सड़क खराब है"

    response = process_input(
        "text",
        complaint
    )

    print(response)