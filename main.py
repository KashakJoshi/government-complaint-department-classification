from src.config.configuration import ConfigurationManager

from src.components.data_cleaning import DataCleaning
from src.components.hindi_nlp import HindiNLP
from src.components.feature_engineering import FeatureEngineering

from src.logger.logger import logger
from src.exception.exception import CustomException

import pandas as pd
import sys



def run_pipeline():

    try:

        logger.info("Pipeline Started")


        config = ConfigurationManager()


        # ==========================
        # Data Cleaning Phase
        # ==========================

        logger.info("Data Cleaning Phase Started")

        data_cleaning_config = (
            config.get_data_cleaning_config()
        )

        data_cleaning = DataCleaning(
            data_cleaning_config
        )

        raw_df = pd.read_csv(
            "data/raw/dataset.csv"
        )

        cleaned_df = data_cleaning.clean_data(
            raw_df
        )

        logger.info(
            "Data Cleaning Phase Completed"
        )


        # ==========================
        # Hindi NLP Phase
        # ==========================

        logger.info(
            "Hindi NLP Phase Started"
        )

        hindi_nlp_config = (
            config.get_hindi_nlp_config()
        )

        hindi_nlp = HindiNLP(
            hindi_nlp_config
        )

        processed_df = hindi_nlp.process(
            cleaned_df
        )

        logger.info(
            "Hindi NLP Phase Completed"
        )


        # ==========================
        # Feature Engineering Phase
        # ==========================

        logger.info(
            "Feature Engineering Phase Started"
        )

        feature_engineering_config = (
            config.get_feature_engineering_config()
        )

        feature_engineering = FeatureEngineering(
            feature_engineering_config
        )

        features = feature_engineering.engineer_features(
            processed_df
        )

        logger.info(
            "Feature Engineering Phase Completed"
        )


        print("\nPipeline Completed Successfully")

        print("\nProcessed Dataset:")
        print(processed_df.head())

        print("\nFeature Keys:")
        print(features.keys())


    except Exception as e:

        logger.error(
            CustomException(e, sys)
        )

        raise CustomException(e, sys)



if __name__ == "__main__":

    run_pipeline()