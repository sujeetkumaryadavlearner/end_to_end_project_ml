import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from mlProject.constants import *
from mlProject.utils.common import read_yaml , create_directories
from sklearn.preprocessing import LabelEncoder,OrdinalEncoder
from mlProject.entity.config_entity import DataTransformationConfig
import os


class DataTranformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config
        create_directories([self.config.root_dir])
    def lable_data(self)->pd.DataFrame:
        df = pd.read_csv(self.config.data_dir)
        categoried_1=[['Fair', 'Good', 'Very Good', 'Premium', 'Ideal']]
        clarity_mapping = {'I1':0,'SI2': 1, 'SI1': 2, 'VS2': 3, 'VS1': 4, 'VVS2': 5, 'VVS1': 6, 'IF': 7}
        color_mapping = {'J': 0, 'I': 1, 'H': 2, 'G': 3, 'F': 4, 'E': 5, 'D': 6}

        encoder1=OrdinalEncoder(categories=categoried_1)
        encoder2=OrdinalEncoder(categories=clarity_mapping)
        encoder3=OrdinalEncoder(categories=color_mapping)

        df["cut"]=encoder1.fit_transform(df[["cut"]])
        df["clarity"]=df["clarity"].map(clarity_mapping)
        df["color"]=df["color"].map(color_mapping)

        return df
    
    def transform(self,df):
        df.drop(columns=["Unnamed: 0"], inplace=True)
        df.dropna(inplace=True)
        df.reset_index(drop=True, inplace=True)
        X= df[["price"]]
        Y =df.drop(columns=["price"])
        X_train,X_test,Y_train,Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)
        X_train.to_csv(os.path.join(self.config.root_dir ,"X_train.csv"), index=False)
        X_test.to_csv(os.path.join(self.config.root_dir , "X_test.csv"), index=False) 
        Y_train.to_csv(os.path.join(self.config.root_dir , "Y_train.csv"), index=False)
        Y_test.to_csv(os.path.join(self.config.root_dir , "Y_test.csv"), index=False)
        
