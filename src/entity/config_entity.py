from dataclasses import dataclass


@dataclass(frozen=True)
class ProjectConfig:
    name: str
    version: str
    author: str


@dataclass(frozen=True)
class LoggingConfig:
    log_dir: str
    log_level: str


@dataclass(frozen=True)
class ArtifactConfig:
    root_dir: str


@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: str
    data_path: str
    validation_report_path: str
    required_columns: list[str]
    optional_columns: list[str]
    file_extension: str
    
@dataclass(frozen=True)
class DataCleaningConfig:
    output_file: str
    complaint_column: str
    sender_column: str
    department_column: str
    remove_duplicates: bool
    remove_null_complaints: bool
    remove_null_departments: bool
    
    
@dataclass(frozen=True)
class FeatureEngineeringConfig:
    output_file: str
    label_encoder_path: str
    complaint_column: str
    location_column: str
    department_column: str    


@dataclass(frozen=True)
class ModelConfig:
    model_name: str
    max_length: int
    num_labels: int
    do_lower_case: bool
    device: str


@dataclass(frozen=True)
class TrainingConfig:
    train_size: float
    test_size: float
    random_state: int
    batch_size: int
    learning_rate: float
    epochs: int
    weight_decay: float
    warmup_ratio: float


@dataclass(frozen=True)
class PreprocessingConfig:
    remove_duplicates: bool
    remove_null_values: bool
    normalize_unicode: bool
    remove_extra_spaces: bool


@dataclass(frozen=True)
class InferenceConfig:
    top_k: int


@dataclass(frozen=True)
class DataPathConfig:
    raw_dir: str
    interim_dir: str
    processed_dir: str
    external_dir: str


@dataclass(frozen=True)
class ModelPathConfig:
    model_dir: str
    model_file: str
    tokenizer_dir: str


@dataclass(frozen=True)
class ReportPathConfig:
    report_dir: str


@dataclass(frozen=True)
class NotebookPathConfig:
    notebook_dir: str