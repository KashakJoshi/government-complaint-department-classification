import os
import sys
import re
import pandas as pd

from langdetect import detect
from langdetect.lang_detect_exception import LangDetectException

from src.logger.logger import logger
from src.exception.exception import CustomException
from src.entity.config_entity import DataCleaningConfig
from src.components.location_extractor import LocationExtractor


class DataCleaning:

    def __init__(self, config: DataCleaningConfig):
        self.config = config
        print("DATA CLEANING INIT")
        self.location_extractor = LocationExtractor(
            "data/external/location_dictionary.txt"
        )
        print(self.location_extractor.locations)
    def clean_data(self, dataframe: pd.DataFrame) -> pd.DataFrame:

        try:
            logger.info("Data Cleaning Started")

            df = dataframe.copy()

            # Remove Duplicates
            if self.config.remove_duplicates:
                df.drop_duplicates(inplace=True)

            # Remove Null Complaints
            if self.config.remove_null_complaints:
                df = df[df[self.config.complaint_column].notna()]

            # Remove Null Departments
            if self.config.remove_null_departments:
                df = df[df[self.config.department_column].notna()]

            # Strip Complaint
            df[self.config.complaint_column] = (
                df[self.config.complaint_column]
                .astype(str)
                .str.strip()
            )

            # Strip Department
            df[self.config.department_column] = (
                df[self.config.department_column]
                .astype(str)
                .str.strip()
            )

            # Unicode Cleaning
            df[self.config.complaint_column] = (
                df[self.config.complaint_column]
                .apply(self.clean_unicode)
            )
            
            # Text Normalization
            df[self.config.complaint_column] = (
                df[self.config.complaint_column]
                .apply(self.normalize_text)
            )
            
        

            # Final Dataset
            final_df = pd.DataFrame(
                {
                    "complaint": df[self.config.complaint_column],
                    "department": df[self.config.department_column],
                    "label": df["label"],
                }
            )
            
            print(df["label"].isna().sum())

            os.makedirs(
                os.path.dirname(self.config.output_file),
                exist_ok=True,
            )

            final_df.to_csv(
                self.config.output_file,
                index=False,
                encoding="utf-8-sig",
            )

            logger.info("Data Cleaning Completed Successfully")

            return final_df

        except Exception as e:
            logger.error(CustomException(e, sys))
            raise CustomException(e, sys)

    def detect_language(self, text: str) -> str:

        try:

            text = str(text).strip()

            if len(text) < 3:
                return "unknown"

            return detect(text)

        except LangDetectException:
            return "unknown"

        except Exception:
            return "unknown"

    def clean_unicode(self, text: str) -> str:

        text = str(text)

        text = text.replace("\ufeff", "")
        text = text.replace("\u200b", "")
        text = text.replace("\u200c", "")
        text = text.replace("\u200d", "")
        text = text.replace("\xa0", " ")

        text = re.sub(r"[\r\n\t]+", " ", text)

        return text.strip()
    
    
    def normalize_text(self, text: str) -> str:

        text = str(text)

        # Convert multiple spaces to single space
        text = re.sub(r"\s+", " ", text)

        # Remove leading and trailing spaces
        text = text.strip()

        return text