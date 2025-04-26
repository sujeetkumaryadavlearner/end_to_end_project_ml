import joblib
import numpy as np
import pandas as pd
from pathlib import Path
import os


class PredictionPipeline:
    def __init__(self):
        self.model_path = os.path.join('artifact', 'model_training', 'model.joblib')
        self.model = joblib.load(Path(self.model_path))


    def predict(self, data):
        data_df = pd.DataFrame(data, columns=["carat", "cut", "color", "clarity", "depth", "table", "x", "y", "z"])
        predictions = self.model.predict(data_df)
        return predictions

