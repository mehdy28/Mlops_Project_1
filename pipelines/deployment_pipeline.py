import json
import os
import numpy as np
import pandas as pd
#from materializer.custom_materializer import cs_materializer
from steps.data_ingestion import ingest_data
from steps.data_cleaning import clean_data
from steps.model_development import execute_model_tuning
from steps.model_evaluation import model_evaluation
from steps.deployment_trigger import deployment_trigger
from steps.prediction_service_loader import prediction_service_loader
from steps.dynamic_importer import dynamic_importer
from steps.predictor import predictor
from zenml import pipeline
from zenml.config import DockerSettings
from zenml.constants import DEFAULT_SERVICE_START_STOP_TIMEOUT
from zenml.integrations.constants import MLFLOW, TENSORFLOW
from zenml.integrations.mlflow.steps import mlflow_model_deployer_step

docker_settings = DockerSettings(required_integrations=[MLFLOW])

@pipeline(enable_cache=False, settings={"docker": docker_settings})
def continuous_deployment_pipeline(
    min_f1: float = 0.9,
    workers: int = 3,
    timeout: int = DEFAULT_SERVICE_START_STOP_TIMEOUT,
):
    # Link all the steps artifacts together
    df = ingest_data(csv_path="data/raw_data.csv")
    x_train, x_test, y_train, y_test = clean_data(df)
    model = execute_model_tuning(x_train, x_test, y_train, y_test)
    accuracy ,precision , recall , f_1 = model_evaluation(model,x_test,y_test)
    deployment_decision = deployment_trigger(f1=f_1)
    mlflow_model_deployer_step(
        model=model,
        deploy_decision=deployment_decision,
        workers=workers,
        timeout=timeout,
    )


@pipeline(enable_cache=False, settings={"docker": docker_settings})
def inference_pipeline(pipeline_name: str, pipeline_step_name: str):
    # Link all the steps artifacts together
    batch_data = dynamic_importer()
    model_deployment_service = prediction_service_loader(
        pipeline_name=pipeline_name,
        pipeline_step_name=pipeline_step_name,
        running=False,
    )
    predictor(service=model_deployment_service, data=batch_data)
