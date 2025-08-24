import os
import pandas as pd
import numpy as np
import joblib
from sklearn.model_selection import train_test_split
from src.logger import get_logger
from src.custom_exception import CustomExeption
from config.path_config import *
import sys

logger = get_logger(__name__)

class DataProcessor:
    def __init__(self,input_file,output_dir):
        self.input_file = input_file
        self.output_dir = output_dir

        self.rating_df = None
        self.anime_df = None
        self.X_train_array = None
        self.X_test_array = None
        self.y_train = None
        self.y_test = None

        self.user2user_encoded = {}
        self.user2user_decoded = {}
        self.anime2anime_encoded = {}
        self.anime2anime_decoded = {}

        os.makedirs(self.output_dir,exist_ok=True)
        logger.info("Starting data loading...............")

    def load_data(self,usecols):
        try:
            self.rating_df = pd.read_csv(self.input_file,low_memory=True,usecols=usecols)
            logger.info("Data loaded successfully for data processing.........")
        except Exception as e:
            raise CustomExeption("Failed to load data..",sys)
    
    def filter_users(self,min_rating=50):
        try:
            n_ratings = self.rating_df["user_id"].value_counts()
            self.rating_df = self.rating_df[self.rating_df["user_id"].isin(n_ratings[n_ratings>=50].index)].copy()
            logger.info("Data filtered successfully.......")
        except Exception as e:
            raise CustomExeption("Faild to filter data.......",sys)
        
    def scale_ratings(self):
        try:
            min_rating =min(self.rating_df["rating"])
            max_rating =max(self.rating_df["rating"])

            self.rating_df["rating"] = self.rating_df["rating"].apply(lambda x: (x-min_rating)/(max_rating-min_rating)).values.astype(np.float64)
            logger.info("Data scaling is done..........")
        except Exception as e:
            raise CustomExeption("Faild to Scale data.......")            

