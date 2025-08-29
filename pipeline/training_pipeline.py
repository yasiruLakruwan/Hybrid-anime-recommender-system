from config.path_config import ANIMELIST_CSV, CONFIG_FILE, PROCESSED_DIR
from src.data_processing import DataProcessor
from src.model_training import ModelTraining
from utils.common_function import read_yaml_file


if __name__ == "__main__":

    # Performe data processing
    data_processor = DataProcessor(ANIMELIST_CSV,PROCESSED_DIR)
    data_processor.run()

    # Performe model training
    model_triner = ModelTraining(PROCESSED_DIR)
    model_triner.train_model()