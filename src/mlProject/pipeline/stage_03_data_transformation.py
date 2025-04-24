from mlProject import logger
from mlProject.config.configuration import ConfigurationManager
from mlProject.entity.config_entity import DataTransformationConfig
from mlProject.components.data_transformation import DataTranformation
from mlProject.constants import *
STAGE_NAME = "Data Transformation stage"

class DataTransformationPipeline:
    def __init__(self, config):
        pass

    def main(self):
        config = ConfigurationManager()
        data_transformation_config = config.get_data_transformation_config()
        data_transformation = DataTranformation(config=data_transformation_config)
        data=data_transformation.lable_data()
        data_transformation.transform(data)


if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>>>>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<<<<<")
        data_ingestion_training_pipeline = DataTransformationPipeline(config=ConfigurationManager())
        data_ingestion_training_pipeline.main()
        logger.info(f">>>>>>>>>>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e
