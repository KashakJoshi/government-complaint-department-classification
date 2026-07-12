import whisper

from predict import predict_department


whisper_model = None



def get_whisper_model():

    global whisper_model

    if whisper_model is None:

        whisper_model = whisper.load_model(
            "tiny"
        )

    return whisper_model



def audio_to_text(audio_path):

    try:

        model = get_whisper_model()


        result = model.transcribe(
            audio_path,
            language="hi"
        )


        text = result["text"].strip()


        if not text:

            raise ValueError(
                "No speech detected in audio"
            )


        return text


    except Exception as e:

        raise Exception(
            f"Audio processing failed: {str(e)}"
        )



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
            "error": str(e)
        }