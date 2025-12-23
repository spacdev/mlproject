import os
import sys
import pandas as pd
from sklearn.model_selection import train_test_split # type: ignore
from src.exception import CustomException
from src.logger import logging
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    train_set: str = os.path.join('artifacts', 'train.csv')
    test_set: str = os.path.join('artifacts', 'test.csv')
    data: str = os.path.join('artifacts', 'data.csv')

def ingest_data():
    '''
    reads data from a csv datasource and split it into train, test
    returns the train, test path
    '''
    try:
        logging.info('data ingestion')
        df = pd.read_csv('notebooks/StudentsPerformance.csv')  # type: ignore
        
        logging.info('dataset read')
        #make artifacts directory if not already created
        os.makedirs(os.path.dirname(DataIngestionConfig.data), exist_ok=True)
        df.to_csv(DataIngestionConfig.data,header=True, index=False)
        train, test = train_test_split(df, test_size=0.2, random_state=42) # type: ignore
        train.to_csv(DataIngestionConfig.train_set,header=True, index=False) # type: ignore
        test.to_csv(DataIngestionConfig.test_set, header=True, index=False) # type: ignore
        logging.info('dataset split into train and test')
        return DataIngestionConfig.train_set, DataIngestionConfig.test_set
    except Exception as e:
        logging.error('something went wrong ingesting data')
        raise CustomException(e, sys) # type: ignore


    


