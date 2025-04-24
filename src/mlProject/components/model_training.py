from sklearn.tree import DecisionTreeRegressor
from mlProject.utils.common import create_directories
import os
import joblib
from mlProject.entity.config_entity import ModelTrainingConfig
import pandas as pd
from mlProject.constants import *
from mlProject.utils.common import read_yaml , create_directories
from mlProject.entity.config_entity import ModelTrainingConfig
from mlProject.constants import *
from mlProject.utils.common import read_yaml , create_directories
from mlProject.entity.config_entity import ModelTrainingConfig
from mlProject.constants import *


class ModelTraning:
    def __init__(self, config: ModelTrainingConfig):
        create_directories([config.root_dir])
        self.config = config
        self.model = DecisionTreeRegressor(max_depth=self.config.max_depth, min_samples_leaf=self.config.min_samples_leaf)
        self.X_train = pd.read_csv(self.config.X_data_train_dir)
        self.Y_train = pd.read_csv(self.config.Y_data_train_dir)
        self.X_test = pd.read_csv(self.config.X_data_test_dir)
        self.Y_test = pd.read_csv(self.config.Y_data_test_dir)

    def train_model(self):
        self.model.fit(self.X_train, self.Y_train)
        joblib.dump(self.model, os.path.join(self.config.root_dir, self.config.model_name))