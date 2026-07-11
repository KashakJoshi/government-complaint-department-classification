from dataclasses import dataclass


@dataclass(frozen=True)
class DataValidationArtifact:
    validated_data_path: str
    validation_report_path: str


@dataclass(frozen=True)
class FeatureEngineeringArtifact:
    processed_data_path: str
    label_encoder_path: str


@dataclass(frozen=True)
class ModelTrainerArtifact:
    trained_model_path: str
    tokenizer_path: str


@dataclass(frozen=True)
class ModelEvaluationArtifact:
    metrics_file_path: str
    confusion_matrix_path: str


@dataclass(frozen=True)
class PredictionArtifact:
    prediction_output_path: str