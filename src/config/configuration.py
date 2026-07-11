import sys

from src.utils.common import read_yaml
from src.exception.exception import CustomException

from src.constants.constants import (
    CONFIG_FILE,
    MODEL_CONFIG_FILE,
    PARAMS_FILE,
    PATHS_FILE,
)

from src.entity.config_entity import (
    ProjectConfig,
    LoggingConfig,
    ArtifactConfig,
    DataValidationConfig,
    ModelConfig,
    TrainingConfig,
    PreprocessingConfig,
    InferenceConfig,
    DataPathConfig,
    ModelPathConfig,
    ReportPathConfig,
    NotebookPathConfig,
)


class ConfigurationManager:
    """
    Central Configuration Manager
    """

    def __init__(self):
        try:
            self.config = read_yaml(CONFIG_FILE)
            self.model = read_yaml(MODEL_CONFIG_FILE)
            self.params = read_yaml(PARAMS_FILE)
            self.paths = read_yaml(PATHS_FILE)

        except Exception as e:
            raise CustomException(e, sys)

    def get_project_config(self) -> ProjectConfig:

        project = self.config["project"]

        return ProjectConfig(
            name=project["name"],
            version=project["version"],
            author=project["author"],
        )

    def get_logging_config(self) -> LoggingConfig:

        logging = self.config["logging"]

        return LoggingConfig(
            log_dir=logging["log_dir"],
            log_level=logging["log_level"],
        )

    def get_artifact_config(self) -> ArtifactConfig:

        artifact = self.config["artifacts"]

        return ArtifactConfig(
            root_dir=artifact["root_dir"],
        )

    def get_data_validation_config(self) -> DataValidationConfig:

        artifact = self.get_artifact_config()

        return DataValidationConfig(
            root_dir=f"{artifact.root_dir}/data_validation",
            data_path="data/raw/dataset.csv",
            validation_report_path=f"{artifact.root_dir}/data_validation/validation_report.json",
            required_columns=self.config["dataset"]["required_columns"],
            file_extension=self.config["dataset"]["file_extension"],
        )

    def get_model_config(self) -> ModelConfig:

        model = self.model["model"]
        tokenizer = self.model["tokenizer"]
        training = self.model["training"]

        return ModelConfig(
            model_name=model["name"],
            max_length=model["max_length"],
            num_labels=model["num_labels"],
            do_lower_case=tokenizer["do_lower_case"],
            device=training["device"],
        )

    def get_training_config(self) -> TrainingConfig:

        training = self.params["training"]

        return TrainingConfig(
            train_size=training["train_size"],
            test_size=training["test_size"],
            random_state=training["random_state"],
            batch_size=training["batch_size"],
            learning_rate=training["learning_rate"],
            epochs=training["epochs"],
            weight_decay=training["weight_decay"],
            warmup_ratio=training["warmup_ratio"],
        )

    def get_preprocessing_config(self) -> PreprocessingConfig:

        preprocessing = self.params["preprocessing"]

        return PreprocessingConfig(
            remove_duplicates=preprocessing["remove_duplicates"],
            remove_null_values=preprocessing["remove_null_values"],
            normalize_unicode=preprocessing["normalize_unicode"],
            remove_extra_spaces=preprocessing["remove_extra_spaces"],
        )

    def get_inference_config(self) -> InferenceConfig:

        inference = self.params["inference"]

        return InferenceConfig(
            top_k=inference["top_k"],
        )

    def get_data_paths(self) -> DataPathConfig:

        data = self.paths["data"]

        return DataPathConfig(
            raw_dir=data["raw_dir"],
            interim_dir=data["interim_dir"],
            processed_dir=data["processed_dir"],
            external_dir=data["external_dir"],
        )

    def get_model_paths(self) -> ModelPathConfig:

        model = self.paths["models"]

        return ModelPathConfig(
            model_dir=model["model_dir"],
            model_file=model["model_file"],
            tokenizer_dir=model["tokenizer_dir"],
        )

    def get_report_paths(self) -> ReportPathConfig:

        reports = self.paths["reports"]

        return ReportPathConfig(
            report_dir=reports["report_dir"],
        )

    def get_notebook_paths(self) -> NotebookPathConfig:

        notebook = self.paths["notebooks"]

        return NotebookPathConfig(
            notebook_dir=notebook["notebook_dir"],
        )