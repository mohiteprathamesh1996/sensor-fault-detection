from sensor.configuration.mongo_db_connection import MongoDBClient
from sensor.exception import SensorException
import os,sys
import pandas as pd
from sensor.logger import logging
from sensor.pipeline import training_pipeline
from sensor.pipeline.training_pipeline import TrainPipeline
from sensor.utils.main_utils import read_yaml_file
from sensor.constant.training_pipeline import SAVED_MODEL_DIR
from fastapi import FastAPI
from sensor.constant.application import APP_HOST, APP_PORT
from starlette.responses import RedirectResponse
from fastapi import File, UploadFile
from uvicorn import run as app_run
from fastapi.responses import Response
from sensor.ml.model.estimator import ModelResolver,TargetValueMapping
from sensor.utils.main_utils import load_object
from fastapi.middleware.cors import CORSMiddleware



def main():
    try:
        training_pipeline = TrainPipeline()
        training_pipeline.run_pipeline()
    except Exception as e:
        print(e)
        logging.exception(e)


if __name__=="__main__":
    main()
    # set_env_variable(env_file_path)
    # app_run(app, host=APP_HOST, port=APP_PORT)