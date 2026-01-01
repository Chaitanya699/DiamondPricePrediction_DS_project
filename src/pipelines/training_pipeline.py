import os
import pandas as pd
from src.logger import logging
from src.exception import CustomException
from src.components.data_ingestion import DataIngestion
from src.components.model_trainer import ModelTrainer

import sys


if __name__ == "__main__":
    obj= DataIngestion()
    train_data, test_data = obj.initiate_data_ingestion()
    print(train_data, test_data)
    from src.components.data_transformation import DataTransformation
    data_transformation = DataTransformation()
    train_arr, test_arr, _ = data_transformation.initiate_data_transformation(train_data, test_data)
    print(train_arr, test_arr)
    model_trainer = ModelTrainer()
    model_trainer.initate_model_training(train_arr, test_arr)

    logging.info("Model training is completed")
   