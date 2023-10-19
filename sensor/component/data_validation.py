from sensor.exception import SensorException
from sensor.logger import logging
from sensor.constant.training_pipeline import SCHEMA_FILE_PATH
from sensor.entity.artifact_entity import DataIngestionArtifact, DataValidationArtifact
from sensor.entity.config_entity import DataValidationConfig
from sensor.utils.main_utils import read_yaml_file
import pandas as pd
import os, sys

class DataValidation:

    def __init__(
            self, 
            data_ingestion_artifact:DataIngestionArtifact,
            data_validation_config: DataValidationConfig
            ):
        try:
            self.data_ingestion_artifact = data_ingestion_artifact
            self.data_validation_config = data_validation_config
            self._schema_config = read_yaml_file(file_path=SCHEMA_FILE_PATH)
        except Exception as e:
            raise Exception(e, sys)

    def drop_zero_std_dev_cols(self, dataframe:pd.DataFrame)->bool:
        pass

    def validate_number_of_columns(self, dataframe:pd.DataFrame)->bool:
        try:
            number_of_columns = self._schema_config["columns"]

            if len(dataframe.columns) == number_of_columns:
                return True
            
            return False
        except Exception as e:
            raise Exception(e, sys)
        

    def is_numerical_column_exist(self, dataframe:pd.DataFrame)->bool:
        try:
            numerical_columns = self._schema_config["numerical_columns"]
            dataframe_columns = dataframe.columns

            numerical_columns_present = True
            missing_numerical_columns = []
            for num_column in numerical_columns:
                if num_column not in dataframe_columns:
                    numerical_columns_present = False
                    missing_numerical_columns.append(num_column)

            logging.info(f"Missing numerical columns: [{missing_numerical_columns}]")
            return numerical_columns_present


        except Exception as e:
            raise Exception(e, sys)

    @staticmethod
    def read_data(file_path)->pd.DataFrame:
        try:
            return pd.read_csv(file_path)
        except Exception as e:
            raise SensorException(e, sys)

    def detect_dataset_drift(self):
        pass

    def initiate_data_validation(self) -> DataIngestionArtifact:
        try:
            error_message = ""
            # Define file path
            train_file_path = self.data_ingestion_artifact.trained_file_path
            test_file_path = self.data_ingestion_artifact.test_file_path

            # Reading data from train and test file location
            train_dataframe = DataValidation.read_data(train_file_path)
            test_dataframe = DataValidation.read_data(test_file_path)

            # Validate number of columns
            status = self.validate_number_of_columns(dataframe=train_dataframe)
            if not status:
                error_message=f"{error_message}Train dataframe does not contain all columns\n"

            status = self.validate_number_of_columns(dataframe=test_dataframe)
            if not status:
                error_message=f"{error_message}Test dataframe does not contain all columns\n"

            # Validate numerical columns
            status = self.is_numerical_column_exist(dataframe=train_dataframe)
            if not status:
                error_message=f"{error_message}Train dataframe does not contain all numerical columns\n"

            status = self.is_numerical_column_exist(dataframe=test_dataframe)
            if not status:
                error_message=f"{error_message}Test dataframe does not contain all numerical columns\n"

            if len(error_message) > 0:
                raise Exception(error_message)
            

            # Let's generate data drift report to ensure training & testing datasets are from the same distribution 
            # If NOT you've to readjust the logic for train_test_split and get similar distribution for both train & test
            # List of libraries: Evidently AI, TensorFlow data validation, Scipy's ks_2samp

        except Exception as e:
            raise SensorException(e, sys)