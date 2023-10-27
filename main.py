from sensor.configuration.mongo_db_connection import MongoDBClient
from sensor.exception import SensorException
from sensor.logger import logging
import os, sys
from sensor.pipeline.training_pipeline import TrainPipeline
from sensor.constant.application import APP_HOST, APP_PORT
from fastapi import FastAPI
from uvicorn import run as app_run


if __name__ == "__main__":
    try:
        train_pipeline = TrainPipeline()
        train_pipeline.run_pipeline()
    except Exception as e:
        print(e)
        logging.exception(e)