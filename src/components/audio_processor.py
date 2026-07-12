import whisper

from src.predict import predict_department


# =========================
# Load Whisper Base
# =========================

whisper_model = whisper.load_model("base")


# =========================
# Audio To Text
# =========================

def audio_to_text(audio_path):

    result = whisper_model.transcribe(
        audio_path,
        language="hi",
        task="transcribe",
        fp16=False,
        temperature=0,
        condition_on_previous_text=False,
        initial_prompt="यह हिंदी भाषा में एक सरकारी शिकायत है। कृपया केवल हिंदी देवनागरी में लिखें।"
    )

    print("Detected Language:", result.get("language"))

    text = result["text"]
    print("RAW TEXT:")

    print(repr(text))

    return text.strip()


# =========================
# Complete Audio Pipeline
# =========================

def process_audio(audio_path):

    try:

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


    except Exception as e:

        return {
            "error": f"Audio processing failed: {str(e)}"
        }