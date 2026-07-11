import os
import sys

from src.utils.common import read_yaml
from src.exception.exception import CustomException

from src.entity.config_entity import (
    ProjectConfig,
    LoggingConfig,
    ArtifactConfig,
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
    Reads all YAML files once and provides configuration objects.
    """

    def __init__(self):

        try:

            self.config = read_yaml("configs/config.yaml")
            self.model = read_yaml("configs/model.yaml")
            self.params = read_yaml("configs/params.yaml")
            self.paths = read_yaml("configs/paths.yaml")

        except Exception as e:
            raise CustomException(e, sys)

    def get_project_config(self):

        project = self.config["project"]

        return ProjectConfig(
            name=project["name"],
            version=project["version"],
            author=project["author"],
        )

    def get_logging_config(self):

        logging = self.config["logging"]

        return LoggingConfig(
            log_dir=logging["log_dir"],
            log_level=logging["log_level"],
        )

    def get_artifact_config(self):

        artifact = self.config["artifacts"]

        return ArtifactConfig(
            root_dir=artifact["root_dir"],
        )

    def get_model_config(self):

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

    def get_training_config(self):

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

    def get_preprocessing_config(self):

        preprocessing = self.params["preprocessing"]

        return PreprocessingConfig(
            remove_duplicates=preprocessing["remove_duplicates"],
            remove_null_values=preprocessing["remove_null_values"],
            normalize_unicode=preprocessing["normalize_unicode"],
            remove_extra_spaces=preprocessing["remove_extra_spaces"],
        )

    def get_inference_config(self):

        inference = self.params["inference"]

        return InferenceConfig(
            top_k=inference["top_k"],
        )

    def get_data_paths(self):

        data = self.paths["data"]

        return DataPathConfig(
            raw_dir=data["raw_dir"],
            interim_dir=data["interim_dir"],
            processed_dir=data["processed_dir"],
            external_dir=data["external_dir"],
        )

    def get_model_paths(self):

        model = self.paths["models"]

        return ModelPathConfig(
            model_dir=model["model_dir"],
            model_file=model["model_file"],
            tokenizer_dir=model["tokenizer_dir"],
        )

    def get_report_paths(self):

        reports = self.paths["reports"]

        return ReportPathConfig(
            report_dir=reports["report_dir"],
        )

    def get_notebook_paths(self):

        notebook = self.paths["notebooks"]

        return NotebookPathConfig(
            notebook_dir=notebook["notebook_dir"],
        )