import joblib
import numpy as np
import pandas as pd
from pathlib import Path


class PredictionPipeline:
    def __init__(self):
        self.model=joblib.load(Path('artifact\model_training\model.joblib'))

    def predict(self, data):
        predictions = self.model.predict(data)
        return predictions
    
