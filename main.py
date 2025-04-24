from mlProject import logger
from mlProject.config.configuration import ConfigurationManager
from mlProject.entity.config_entity import DataIngestionConfig
from mlProject.components.data_ingestion import DataIngestion
from mlProject.constants import *
from mlProject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
STAGE_NAME = "Data Ingestion stage"

try:
    logger.info(f">>>>>>>>>>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<<<<<")
    data_ingestion_training_pipeline = DataIngestionTrainingPipeline(config=ConfigurationManager())
    data_ingestion_training_pipeline.main()
    logger.info(f">>>>>>>>>>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e