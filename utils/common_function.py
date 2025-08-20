## Common functions for the project 
import yaml
import os
from src.custom_exception import CustomExeption
from src.logger import get_logger
import pandas as pd

logger = get_logger(__name__)

# function for reading yamal file 

def read_yaml_file(filepath):
    try:
        logger.info("Reading config.yaml file")
        if not os.path.exists(filepath):
            raise FileNotFoundError("File is not in the directry...!")
        
        with open(filepath,'r') as f:
            config = yaml.safe_load(f)
            return config
        
    except Exception as e:
        logger.error("Error hapenign loading yaml file.....")
        raise CustomExeption("Error loading yaml file",e)
    
# function to read csv file

def read_csv_file(filepath):
    try:
        logger.info("Srarting reading csv file")

        if not os.path.exists(filepath):

            logger.error('CSV file not in the directry..')
            raise FileNotFoundError("File not in the given directry....!")
        
        return pd.read_csv(filepath)
    
    except Exception as e:
        logger.error("CSV file not loaded...")
        raise CustomExeption("CSV file not loaded..",e)