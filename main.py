from src.config.configuration import ConfigurationManager
from src.components.data_cleaning import DataCleaning
from src.components.hindi_nlp import HindiNLP

import pandas as pd


config = ConfigurationManager()


# Data Cleaning Phase
data_cleaning_config = config.get_data_cleaning_config()

data_cleaning = DataCleaning(data_cleaning_config)

raw_df = pd.read_csv(
    "data/raw/dataset.csv"
)

cleaned_df = data_cleaning.clean_data(raw_df)


# Hindi NLP Phase
hindi_nlp_config = config.get_hindi_nlp_config()

hindi_nlp = HindiNLP(hindi_nlp_config)

processed_df = hindi_nlp.process(cleaned_df)


print(processed_df.head())