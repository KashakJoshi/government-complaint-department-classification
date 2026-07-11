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
    DataCleaningConfig,
    FeatureEngineeringConfig,
    TextInputConfig,
    ModelConfig,
    OCRConfig,
    TrainingConfig,
    HindiNLPConfig,
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
            optional_columns=self.config["dataset"]["optional_columns"],
            file_extension=self.config["dataset"]["file_extension"],
        )
        
    def get_data_cleaning_config(self) -> DataCleaningConfig:

        cleaning = self.config["data_cleaning"]

        return DataCleaningConfig(
            output_file=cleaning["output_file"],
            complaint_column=cleaning["complaint_column"],
            sender_column=cleaning["sender_column"],
            department_column=cleaning["department_column"],
            remove_duplicates=cleaning["remove_duplicates"],
            remove_null_complaints=cleaning["remove_null_complaints"],
            remove_null_departments=cleaning["remove_null_departments"],
    )
    def get_feature_engineering_config(self) -> FeatureEngineeringConfig:

        feature = self.config["feature_engineering"]

        return FeatureEngineeringConfig(
            output_file=feature["output_file"],
            label_encoder_path=feature["label_encoder_path"],
            complaint_column=feature["complaint_column"],
            location_column=feature["location_column"],
            department_column=feature["department_column"],
        )
        
    def get_text_input_config(self) -> TextInputConfig:

        text_config = self.config["text_input"]

        return TextInputConfig(
            max_text_length=text_config["max_text_length"],
            min_text_length=text_config["min_text_length"],
            accepted_input_type=text_config["accepted_input_type"],
            remove_leading_trailing_spaces=text_config["remove_leading_trailing_spaces"],
            convert_to_string=text_config["convert_to_string"],
        )    
        
    def get_hindi_nlp_config(self) -> HindiNLPConfig:

        hindi_nlp = self.config["hindi_nlp"]

        return HindiNLPConfig(
            normalize_spaces=hindi_nlp["normalize_spaces"],
            normalize_tabs=hindi_nlp["normalize_tabs"],
            normalize_newlines=hindi_nlp["normalize_newlines"],
            output_file=hindi_nlp["output_file"],
            remove_special_characters=hindi_nlp["remove_special_characters"],
            evaluate_numbers=hindi_nlp["evaluate_numbers"],
            analyze_stopwords=hindi_nlp["analyze_stopwords"],
            evaluate_stemming=hindi_nlp["evaluate_stemming"],
            evaluate_lemmatization=hindi_nlp["evaluate_lemmatization"],
        )

    def get_ocr_config(self) -> OCRConfig:

        ocr = self.config["ocr"]

        return OCRConfig(
            supported_formats=ocr["supported_formats"],
            languages=ocr["languages"],
            use_gpu=ocr["use_gpu"],
            min_image_size=ocr["min_image_size"],
            max_image_size=ocr["max_image_size"],
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