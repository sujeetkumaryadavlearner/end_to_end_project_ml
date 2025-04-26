from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from mlProject import logger
from mlProject.config.configuration import ConfigurationManager
from mlProject.entity.config_entity import ModelEvaluationConfig
import os
from mlProject.components.model_evlauation import ModelEvaluation
from mlProject.utils.common import read_yaml , create_directories


STAGE_NAME = "Model Evaluation stage"

class ModelEvaluationPipeline:
    def __init__(self, config: ConfigurationManager):
        self.config = config

    def main(self):
        model_evaluation_config = self.config.get_evaluation_config()
        model_evaluation = ModelEvaluation(config=model_evaluation_config)
        model_evaluation.evaluate_model()



if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>>>>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<<<<<")
        config = ConfigurationManager()
        model_evaluation_pipeline = ModelEvaluationPipeline(config=config)
        model_evaluation_pipeline.main()
        logger.info(f">>>>>>>>>>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e