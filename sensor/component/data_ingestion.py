from sensor.exception import SensorException
from sensor.logger import logging
from sensor.entity.config_entity import DataIngestionConfig
from sensor.entity.artifact_entity import DataIngestionArtifact
from pandas import DataFrame
import os, sys

class DataIngestion():

    def __init__(self, data_ingestion_config:DataIngestionConfig):
        try:
            self.data_ingestion_config = data_ingestion_config
        except Exception as e:
            raise SensorException(e, sys)
        
    def export_data_into_feature_store(self)->DataFrame: 
        """Export MongoDB collection record as dataframe into feature store"""
        pass

    def split_data_as_train_test(self, dataframe: DataFrame):
        """Feature stored in dataset to be split into train & test"""

    def initiate_data_ingestion(self) -> DataIngestionArtifact:
        try:
            pass
        except Exception as e:
            raise SensorException(e, sys)






