from src.config.configuration import ConfigurationManager
from src.components.data_validation import DataValidation


if __name__ == "__main__":

    config = ConfigurationManager()

    validation_config = config.get_data_validation_config()

    validation = DataValidation(validation_config)

    artifact = validation.validate_dataset()

    print(artifact)