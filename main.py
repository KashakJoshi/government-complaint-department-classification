import pandas as pd

from src.config.configuration import ConfigurationManager
from src.components.feature_engineering import FeatureEngineering


if __name__ == "__main__":

    config = ConfigurationManager()

    feature_config = config.get_feature_engineering_config()

    df = pd.read_csv("data/interim/cleaned_dataset.csv")

    feature_engineering = FeatureEngineering(feature_config)

    processed_df = feature_engineering.engineer_features(df)

    print(processed_df.head().to_markdown(index=False))