import os
import io
import pandas as pd
from google.cloud import storage
from src.logger import get_logger
from src.custom_exception import CustomExeption
from config.path_config import *
from utils.common_function import read_yaml_file

logger = get_logger(__name__)

class DataIngestion:
    def __init__(self,config):
        self.config = config["data_ingestion"]
        self.bucket_name = self.config["bucket_name"]
        self.file_names = self.config["bucket_file_names"]

        os.makedirs(RAW_DIR,exist_ok=True)
        
        logger.info("Data ingestion started...")

    def download_data_from_gcp(self):
        try:
            client = storage.Client()
            bucket = client.bucket(self.bucket_name)

            for file_name in self.file_names:
                file_path = os.path.join(RAW_DIR,file_name)
                # animelist.csv
                if file_name=="animelist.csv":
                    blob = bucket.blob(file_name)

                    with blob.open('r') as f:
                        df = pd.read_csv(f,nrows=5000)
                    df.to_csv(file_path,index=False)

                    logger.info("Large file detected only downloading 5000 rows")
                
                else:
                    blob = bucket.blob(file_name)
                    blob.download_to_filename(file_path)

                    logger.info("Downloading smaller files, anime and anime_with_synopsis")
        except Exception as e:
            raise CustomExeption("Eror while downloading files",e)
        
    def run(self):
        try:
            logger.info("start data ingestion process..")
            self.download_data_from_gcp()
            logger.info("Data ingestion complete")
        except Exception as e:
            raise CustomExeption(f"CustomExeption : {str(e)}")
        finally:
            logger.info("Data ingestion done...")

if __name__=="__main__":
    dataingestion = DataIngestion(read_yaml_file(CONFIG_FILE))
    dataingestion.run() 
