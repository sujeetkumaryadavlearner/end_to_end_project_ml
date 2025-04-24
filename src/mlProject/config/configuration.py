from mlProject.constants import *
from mlProject.utils.common import read_yaml , create_directories
from mlProject.entity.config_entity import DataIngestionConfig,DataValidationConfig,DataTransformationConfig,ModelTrainingConfig

class ConfigurationManager:
    def __init__(self, config_file_path= CONFIG_FILE_PATH ,params_filepath=PARAMS_FILE_PATH,schema_filepath=SCHEMA_FILE_PATH):
        self.config = read_yaml(config_file_path)
        self.params = read_yaml(params_filepath)
        self.schema = read_yaml(schema_filepath)
        create_directories([self.config.artifacts_root])
    
    def get_data_ingestion_config(self)->DataIngestionConfig:
        config=self.config.data_ingestion
        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_url=config.source_url,
            ingested_data_dir=config.ingested_data_dir
        )
        return data_ingestion_config
    
    def get_data_validation_config(self)->DataValidationConfig:
        config=self.config.data_validation
        create_directories([config.root_dir])

        data_validation_config = DataValidationConfig(
            root_dir=config.root_dir,
            status_file=config.status_file,
            data_dir=config.data_dir
        )
        return data_validation_config

    def get_data_transformation_config(self)->DataTransformationConfig:
        config=self.config.data_transformation
        create_directories([config.root_dir])

        data_transformation_config = DataTransformationConfig(
            root_dir=config.root_dir,
            data_dir=config.data_dir 
        )
        return data_transformation_config

    def get_model_config(self)->ModelTrainingConfig:
        config=self.config.model_training 
        param=self.params.DecisionTreeRegressor
        model_config = ModelTrainingConfig(
            root_dir=config.root_dir,
            X_data_train_dir=config.X_data_train_dir,
            Y_data_train_dir=config.Y_data_train_dir,
            X_data_test_dir=config.X_data_test_dir,
            Y_data_test_dir=config.Y_data_test_dir,
            model_name=config.model_name,
            max_depth=param.max_depth,
            min_samples_leaf=param.min_samples_leaf
        )
        return model_config