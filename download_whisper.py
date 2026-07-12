import whisper

print("Downloading Whisper Tiny...")

whisper_model = whisper.load_model("tiny")

print("Whisper Tiny ready")