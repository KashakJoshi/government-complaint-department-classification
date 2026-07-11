import os
import re
import sys
import pandas as pd

from src.logger.logger import logger
from src.exception.exception import CustomException
from src.entity.config_entity import HindiNLPConfig


class HindiNLP:

    def __init__(self, config: HindiNLPConfig):
        self.config = config

    def normalize_text(self, text: str) -> str:

        text = str(text)

        # Normalize Tabs
        if self.config.normalize_tabs:
            text = text.replace("\t", " ")

        # Normalize New Lines
        if self.config.normalize_newlines:
            text = text.replace("\n", " ")
            text = text.replace("\r", " ")

        # Normalize Multiple Spaces
        if self.config.normalize_spaces:
            text = re.sub(r"\s+", " ", text)

        # Remove Unwanted Special Characters
        if self.config.remove_special_characters:
            text = re.sub(
                r"[^\u0900-\u097F0-9a-zA-Z\s।,!?():/\-]",
                "",
                text,
            )

        return text.strip()

    def process(self, dataframe: pd.DataFrame) -> pd.DataFrame:

        try:

            logger.info("Hindi NLP Preprocessing Started")

            df = dataframe.copy()

            df["complaint"] = df["complaint"].apply(
                self.normalize_text
            )

            os.makedirs(
                os.path.dirname(self.config.output_file),
                exist_ok=True,
            )

            df.to_csv(
                self.config.output_file,
                index=False,
                encoding="utf-8-sig",
            )

            logger.info("Hindi NLP Preprocessing Completed Successfully")

            return df

        except Exception as e:
            logger.error(CustomException(e, sys))
            raise CustomException(e, sys)