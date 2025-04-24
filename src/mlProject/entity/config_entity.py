from pathlib import Path
from dataclasses import dataclass


@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_url: str
    ingested_data_dir: Path

@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    status_file: str
    data_dir: Path

@dataclass(frozen=True)
class DataTransformationConfig:
    root_dir: Path
    data_dir: Path
    

@dataclass(frozen=True)
class ModelTrainingConfig:
    root_dir: Path
    X_data_train_dir:Path
    Y_data_train_dir:Path
    X_data_test_dir:Path
    Y_data_test_dir:Path 
    model_name: str
    max_depth: int
    min_samples_leaf: int
    