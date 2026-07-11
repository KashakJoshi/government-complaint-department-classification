import sys

from src.logger.logger import logger
from src.exception.exception import CustomException
from src.entity.config_entity import TextInputConfig


class TextInput:

    def __init__(self, config: TextInputConfig):
        self.config = config

    def process(self, text):

        try:
            logger.info("Text Input Processing Started")

            # Convert to String
            if self.config.convert_to_string:
                text = str(text)

            # Remove Leading/Trailing Spaces
            if self.config.remove_leading_trailing_spaces:
                text = text.strip()

            # Empty Check
            if len(text) == 0:
                raise ValueError("Input text is empty.")

            # Minimum Length Check
            if len(text) < self.config.min_text_length:
                raise ValueError(
                    f"Text must contain at least {self.config.min_text_length} characters."
                )

            # Maximum Length Check
            if len(text) > self.config.max_text_length:
                raise ValueError(
                    f"Text exceeds maximum allowed length of {self.config.max_text_length} characters."
                )

            logger.info("Text Input Processing Completed Successfully")

            return text

        except Exception as e:
            logger.error(CustomException(e, sys))
            raise CustomException(e, sys)