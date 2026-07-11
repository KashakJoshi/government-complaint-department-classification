import os
import sys
from PIL import Image
import easyocr

from src.logger.logger import logger
from src.exception.exception import CustomException
from src.entity.config_entity import OCRConfig


class OCRPipeline:

    def __init__(self, config: OCRConfig):

        self.config = config

        self.reader = easyocr.Reader(
            self.config.languages,
            gpu=self.config.use_gpu
        )

    def extract_text(self, image_path: str) -> str:

        try:

            logger.info("OCR Pipeline Started")

            if not os.path.exists(image_path):
                raise FileNotFoundError(
                    f"Image not found: {image_path}"
                )

            extension = image_path.split(".")[-1].lower()

            if extension not in self.config.supported_formats:
                raise ValueError(
                    f"Unsupported image format: {extension}"
                )

            image = Image.open(image_path)

            width, height = image.size

            if (
                width < self.config.min_image_size
                or
                height < self.config.min_image_size
            ):
                raise ValueError("Image is too small.")

            if (
                width > self.config.max_image_size
                or
                height > self.config.max_image_size
            ):
                raise ValueError("Image is too large.")

            result = self.reader.readtext(
                image_path,
                detail=0,
                paragraph=True
            )

            text = " ".join(result).strip()

            logger.info("OCR Pipeline Completed Successfully")

            return text

        except Exception as e:
            logger.error(CustomException(e, sys))
            raise CustomException(e, sys)