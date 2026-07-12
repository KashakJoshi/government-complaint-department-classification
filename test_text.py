from src.components.input_router import process_input


audio_path = "data/input/test_audio.mpeg"


response = process_input(
    "audio",
    audio_path
)


print("\nFINAL OUTPUT:")
print(response)