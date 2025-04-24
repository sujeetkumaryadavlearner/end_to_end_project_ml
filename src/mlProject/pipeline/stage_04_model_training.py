from mlProject import logger
from mlProject.config.configuration import ConfigurationManager
from mlProject.entity.config_entity import ModelTrainingConfig
from mlProject.components.model_training import ModelTraning

STAGE_NAME = "Model Training stage"

class ModelTrainingPipeline:
    def __init__(self, config: ConfigurationManager):
        self.config = config

    def main(self):
        model_training_config = self.config.get_model_config()
        model_trainer = ModelTraning(config=model_training_config)
        model_trainer.train_model()


if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>>>>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<<<<<")
        config = ConfigurationManager()
        model_training_pipeline = ModelTrainingPipeline(config=config)
        model_training_pipeline.main()
        logger.info(f">>>>>>>>>>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e
