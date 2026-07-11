import os
import sys
import json
import pandas as pd

from src.logger.logger import logger
from src.exception.exception import CustomException
from src.entity.config_entity import DataValidationConfig
from src.entity.artifact_entity import DataValidationArtifact


class DataValidation:

    def __init__(self, config: DataValidationConfig):
        self.config = config

    def validate_dataset(self) -> DataValidationArtifact:
        try:
            logger.info("Data Validation Started")

            # File Exists
            if not os.path.exists(self.config.data_path):
                raise FileNotFoundError(
                    f"Dataset not found: {self.config.data_path}"
                )

            # File Extension
            if not self.config.data_path.endswith(self.config.file_extension):
                raise ValueError(
                    f"Dataset must be {self.config.file_extension}"
                )

            # Read Dataset
            df = pd.read_csv(self.config.data_path)

            # Empty Dataset
            if df.empty:
                raise ValueError("Dataset is empty.")

            # Required Columns
            missing_columns = [
                column
                for column in self.config.required_columns
                if column not in df.columns
            ]

            if missing_columns:
                raise ValueError(
                    f"Missing Columns: {missing_columns}"
                )

            # Validation Report
            report = {
                "validation_status": True,
                "total_rows": len(df),
                "total_columns": len(df.columns),
                "missing_values": int(df.isnull().sum().sum()),
                "duplicate_rows": int(df.duplicated().sum()),
                "required_columns_present": True
            }

            os.makedirs(self.config.root_dir, exist_ok=True)

            with open(
                self.config.validation_report_path,
                "w",
                encoding="utf-8"
            ) as file:
                json.dump(report, file, indent=4, ensure_ascii=False)

            logger.info("Data Validation Completed Successfully")

            return DataValidationArtifact(
                validation_status=True,
                validated_data_path=self.config.data_path,
                validation_report_path=self.config.validation_report_path
            )

        except Exception as e:
            logger.error(CustomException(e, sys))
            raise CustomException(e, sys)