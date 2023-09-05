from abc import ABC, abstractmethod
from log import logger
from sklearn.model_selection import RandomizedSearchCV

class Model(ABC):
    """
    Abstract base class for all models.
    """

    @abstractmethod
    def train(self, x_train, y_train):
        pass

    @abstractmethod
    def optimize(self, x_train, y_train, x_test, y_test):
        pass

class ModelTuner:
    """
    Class for performing hyperparameter tuning. It uses Model strategy to perform tuning.
    """

    def __init__(self, x_train,x_test, y_train, y_test , model_classes, param_grid):
        self.model_classes = dict(model_classes)  # Make a copy of model_classes as a dictionary
        self.param_grid = param_grid
        self.x_train = x_train
        self.y_train = y_train
        self.x_test = x_test
        self.y_test = y_test

    def train(self, model_name, **kwargs):
        try:
            model_class = self.model_classes[model_name]
            clf = model_class(**kwargs)
            clf.fit(self.x_train, self.y_train)
            logger.info(f"Model {model_name} training successful.")
            return clf
        except Exception as e:
            logger.error(f"Model {model_name} training failed: {str(e)}")
            raise e

    def optimize(self, model_name):
        try:
            model_class = self.model_classes[model_name]
            clf = model_class()
            grid_search = RandomizedSearchCV(clf, param_distributions=self.param_grid[model_name], n_iter=10, cv=5, n_jobs=-1)
            grid_search.fit(self.x_train, self.y_train)

            best_params = grid_search.best_params_
            best_model = grid_search.best_estimator_

            y_pred = best_model.predict(self.x_test)
            logger.info(f"Hyperparameter tuning for {model_name} successful.")
            return best_model, best_params
        except Exception as e:
            logger.error(f"Hyperparameter tuning for {model_name} failed: {str(e)}")
            raise e
