import os
import sys
import joblib
import pandas as pd
import torch

from transformers import AutoTokenizer

from src.logger.logger import logger
from src.exception.exception import CustomException
from src.entity.config_entity import FeatureEngineeringConfig


class FeatureEngineering:

    def __init__(self, config: FeatureEngineeringConfig):

        self.config = config

        self.model_name = "bert-base-multilingual-cased"

        self.tokenizer = AutoTokenizer.from_pretrained(
            self.model_name
        )


    def engineer_features(
        self,
        dataframe: pd.DataFrame
    ):

        try:

            logger.info(
                "Feature Engineering Started"
            )

            df = dataframe.copy()


            # ----------------------------
            # Label Encoding
            # ----------------------------
            df = df.dropna(subset=["label"])
            df["label"] = df["label"].astype(int)


            # ----------------------------
            # Tokenization
            # ----------------------------

            encoded_texts = self.tokenizer(
                df[self.config.complaint_column].tolist(),

                padding="max_length",

                truncation=True,

                max_length=128,

                return_tensors="pt"
            )


            features = {

                "input_ids": encoded_texts["input_ids"],

                "attention_mask": encoded_texts["attention_mask"],

                "labels": torch.tensor(
                    df["label"].values
                )
            }


            # ----------------------------
            # Save Features
            # ----------------------------

            os.makedirs(
                os.path.dirname(
                    self.config.output_file
                ),
                exist_ok=True
            )


            torch.save(
                features,
                self.config.output_file
            )



            logger.info(
                "Feature Engineering Completed Successfully"
            )


            return features


        except Exception as e:

            logger.error(
                CustomException(e, sys)
            )

            raise CustomException(e, sys)