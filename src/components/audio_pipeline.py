import whisper

from predict import predict_department


model = whisper.load_model("tiny")


def audio_to_text(audio_path):

    result = model.transcribe(
        audio_path,
        language="hi"
    )

    return result["text"]



def process_audio(audio_path):

    text = audio_to_text(audio_path)

    result = predict_department(text)

    return {
        "text": text,
        "prediction": result
    }