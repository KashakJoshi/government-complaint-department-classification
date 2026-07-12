from src.components.input_router import process_input


image_path = "data/input/test_image.jpg"


response = process_input(
    "image",
    image_path
)


print("\nFINAL OUTPUT:")
print(response)