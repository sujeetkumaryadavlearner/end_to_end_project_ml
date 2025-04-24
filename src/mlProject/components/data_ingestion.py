from mlProject.constants import *
from mlProject.utils.common import read_yaml , create_directories
from mlProject.entity.config_entity import DataIngestionConfig
from mlProject.entity.config_entity import DataIngestionConfig
import os
import requests
from mlProject import logger

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self):
    # Raw CSV URL
        csv_url = 'https://raw.githubusercontent.com/sujeetkumaryadavlearner/Diamond_price_Pred/main/data/raw/diamonds%20.csv'

        # Define folder and file paths
        folder_path = os.path.join('artifact', 'data_ingestion')
        file_path = os.path.join(folder_path, 'diamond.csv')

        # Create folders if they don't exist
        os.makedirs(folder_path, exist_ok=True)

        # Download the CSV file
        response = requests.get(csv_url)
        response.raise_for_status()  # Check for request errors

        # Save the file
        with open(file_path, 'wb') as file:
            file.write(response.content)

        logger.info(f'CSV file successfully saved at: {file_path}')

