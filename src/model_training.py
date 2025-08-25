import joblib
import numpy as np
import os
from tensorflow.keras.callbacks import ModelCheckpoint,LearningRateScheduler,TensorBoard,EarlyStopping
from src.logger import get_logger
from src.custom_exception import CustomExeption
from src.base_model import BaseModel
from config.path_config import *

logger = get_logger(__name__)

class ModelTraining:
    def __init__(self,data_path):
        self.data_path = data_path
        logger.info("Model training initialized..........")

    def load_data(self):
        try:
            X_train_array = joblib.load(X_TRAIN_ARRAY)
            X_test_array = joblib.load(X_TEST_ARRAY)
            y_train = joblib.load(Y_TRAIN)
            y_test = joblib.load(Y_TEST)

            logger.info("Data loaded successfully.......")
            return X_train_array,X_test_array,y_train,y_test
        
        except Exception as e:
            logger.error("Error while loading the data......")
            raise CustomExeption("Error while loading the data......",e)
        