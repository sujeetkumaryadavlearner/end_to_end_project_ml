from mlProject.constants import *
from mlProject.utils.common import read_yaml , create_directories
from mlProject.entity.config_entity import DataIngestionConfig
from mlProject.entity.config_entity import DataIngestionConfig
import os
import requests
from mlProject import logger
import pandas as pd
from mlProject.entity.config_entity import DataValidationConfig
from mlProject.entity.config_entity import DataValidationConfig
import os
class DataValidation:   
    def __init__(self, config: DataValidationConfig):
        self.config = config

    def validate_data(self):
        # Load the data
        try:
            validation_status=None
            data = pd.read_csv(self.config.data_dir)
            validation_status=True
            with open(self.config.status_file, 'w') as file:
                file.write(f"Data validation status: {validation_status}\n")
            logger.info(f'Data loaded successfully from {self.config.data_dir}')
        except Exception as e:
            logger.error(f'Error loading data: {e}')
    
        return validation_status
        
