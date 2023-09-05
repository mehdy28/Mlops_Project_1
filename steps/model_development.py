from model.model_dev import ModelTuner
from sklearn.metrics import f1_score
from log import logger
import joblib
import pandas as pd
from zenml import step
import mlflow
from zenml.client import Client
from config import model_classes, param_grid 

from sklearn.base import ClassifierMixin

experiment_tracker = Client().active_stack.experiment_tracker

@step(experiment_tracker=experiment_tracker.name)
def execute_model_tuning(
    x_train: pd.DataFrame,
    x_test: pd.DataFrame,
    y_train: pd.Series,
    y_test: pd.Series,
)-> ClassifierMixin:
    best_f1_score = 0
    best_model = None
    best_params = None
    best_model_name = None

    for model_name, model_class in model_classes.items():
        model = model_class()  # Create an instance of the model
        '''
        model_tuner = ModelTuner({model_name: model_class}, param_grid, x_train, y_train, x_test, y_test)
        '''
        model_tuner = ModelTuner(x_train, x_test, y_train, y_test, {model_name: model_class}, param_grid)

        logger.info(f"Training Model {model_name}")
        model_tuner.train(model_name)  # Train the model

        logger.info(f"Optimizing hyperparameters for {model_name}")
        current_best_model, current_best_params = model_tuner.optimize(model_name)

        y_pred = current_best_model.predict(x_test)
        current_f1 = f1_score(y_test, y_pred)  # Calculate F1 score

        if current_f1 > best_f1_score:
            best_f1_score = current_f1
            best_model_name = model_name
            best_params = current_best_params
            best_model = current_best_model

    print(f"Best Model - {best_model_name} - Best F1 Score: {best_f1_score}")
    print(f"Best Parameters: {best_params}")

    saved_model_filename = f"saved_model/{best_model_name}_best_model.pkl"
    joblib.dump(best_model, saved_model_filename)
    logger.info(f"Best model saved as '{saved_model_filename}'")

    return best_model
