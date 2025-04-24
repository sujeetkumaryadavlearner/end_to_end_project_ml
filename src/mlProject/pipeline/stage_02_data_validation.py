from mlProject import logger
from mlProject.config.configuration import ConfigurationManager
from mlProject.entity.config_entity import DataValidationConfig
from mlProject.components.data_validation import DataValidation
from mlProject.utils.common import read_yaml , create_directories
from mlProject.constants import *
STAGE_NAME = "Data Validation stage"

class DataValidationPipeline:
    def __init__(self, config):
        pass

    def main(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_ingestion_config()
        data_validation = DataValidation(config=data_validation_config)
        data_validation.validate_data()

if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>>>>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<<<<<")
        data_validation_training_pipeline = DataValidationPipeline(config=ConfigurationManager())
        data_validation_training_pipeline.main()
        logger.info(f">>>>>>>>>>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e
