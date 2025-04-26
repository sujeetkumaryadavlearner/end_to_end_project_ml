from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from mlProject import logger
from mlProject.config.configuration import ConfigurationManager
from mlProject.entity.config_entity import ModelEvaluationConfig
import pandas as pd
import joblib
import os

class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config

    def evaluate_model(self):
       model=joblib.load(self.config.model_dir)
       X_test = pd.read_csv(self.config.X_data_test_dir)
       Y_test = pd.read_csv(self.config.Y_data_test_dir)
       y_pred = model.predict(X_test)
       r2_scoree=r2_score(Y_test, y_pred)
       mse = mean_squared_error(Y_test, y_pred)

       with open(self.config.report_dir, 'w') as report_file:
           report_file.write(f"R2 Score: {r2_scoree}\n")
           report_file.write(f"Mean Squared Error: {mse}\n")
           logger.info(f"Model evaluation report saved at {self.config.report_dir}")      
       
