from mlProject import logger
from mlProject.config.configuration import ConfigurationManager
from mlProject.entity.config_entity import DataIngestionConfig
from mlProject.components.data_ingestion import DataIngestion
from mlProject.constants import *
STAGE_NAME = "Data Ingestion stage"

class DataIngestionTrainingPipeline:
    def __init__(self, config):
        pass

    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()


if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>>>>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<<<<<")
        data_ingestion_training_pipeline = DataIngestionTrainingPipeline(config=ConfigurationManager())
        data_ingestion_training_pipeline.main()
        logger.info(f">>>>>>>>>>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e
