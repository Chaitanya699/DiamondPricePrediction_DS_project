import os
import pandas as pd
from src.logger import logging
from src.exception import CustomException
from src.components.data_ingestion import DataIngestion
import sys


if __name__ == "__main__":
    obj= DataIngestion()
    train_data, test_data = obj.initiate_data_ingestion()
    print(train_data, test_data)