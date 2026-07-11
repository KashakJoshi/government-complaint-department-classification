import whisper

from predict import predict_department


# Lightweight model
whisper_model = whisper.load_model("tiny")


def audio_to_text(audio_path):

    result = whisper_model.transcribe(
        audio_path,
        language="hi"
    )

    text = result["text"]

    return text



def process_audio(audio_path):

    text = audio_to_text(
        audio_path
    )

    prediction = predict_department(
        text
    )

    return {
        "text": text,
        "prediction": prediction
    }