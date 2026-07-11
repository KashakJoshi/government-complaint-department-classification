import os
import sys
import joblib
import pandas as pd

from sklearn.preprocessing import LabelEncoder

from src.logger.logger import logger
from src.exception.exception import CustomException
from src.entity.config_entity import FeatureEngineeringConfig


class FeatureEngineering:

    def __init__(self, config: FeatureEngineeringConfig):
        self.config = config

    def engineer_features(self, dataframe: pd.DataFrame) -> pd.DataFrame:

        try:
            logger.info("Feature Engineering Started")

            df = dataframe.copy()

            label_encoder = LabelEncoder()

            df["label"] = label_encoder.fit_transform(
                df[self.config.department_column]
            )

            os.makedirs(
                os.path.dirname(self.config.output_file),
                exist_ok=True,
            )

            os.makedirs(
                os.path.dirname(self.config.label_encoder_path),
                exist_ok=True,
            )

            df.to_csv(
                self.config.output_file,
                index=False,
                encoding="utf-8-sig",
            )

            joblib.dump(
                label_encoder,
                self.config.label_encoder_path,
            )

            logger.info("Feature Engineering Completed Successfully")

            return df

        except Exception as e:
            logger.error(CustomException(e, sys))
            raise CustomException(e, sys)