from log import logger 
import numpy as np
from abc import ABC, abstractmethod
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score



class BinaryClassificationEvaluation(ABC):
    """
    Abstract Class defining the strategy for evaluating binary classification model performance
    """
    @abstractmethod
    def calculate_score(self, y_true: np.ndarray, y_pred: np.ndarray) -> float:
        pass


class Accuracy(BinaryClassificationEvaluation):
    """
    Evaluation strategy that uses Accuracy for binary classification
    """
    def calculate_score(self, y_true: np.ndarray, y_pred: np.ndarray) -> float:
        """
        Args:
            y_true: np.ndarray
            y_pred: np.ndarray
        Returns:
            accuracy: float
        """
        try:
            logger.info("Entered the calculate_score method of the Accuracy class")
            accuracy = accuracy_score(y_true, y_pred)
            logger.info("The accuracy score value is: " + str(accuracy))
            return accuracy
        except Exception as e:
            logger.error(
                "Exception occurred in calculate_score method of the Accuracy class. Exception message: " + str(e)
            )
            raise e


class Precision(BinaryClassificationEvaluation):
    """
    Evaluation strategy that uses Precision for binary classification
    """
    def calculate_score(self, y_true: np.ndarray, y_pred: np.ndarray) -> float:
        """
        Args:
            y_true: np.ndarray
            y_pred: np.ndarray
        Returns:
            precision: float
        """
        try:
            logger.info("Entered the calculate_score method of the Precision class")
            precision = precision_score(y_true, y_pred)
            logger.info("The precision score value is: " + str(precision))
            return precision
        except Exception as e:
            logger.error(
                "Exception occurred in calculate_score method of the Precision class. Exception message: " + str(e)
            )
            raise e


class Recall(BinaryClassificationEvaluation):
    """
    Evaluation strategy that uses Recall for binary classification
    """
    def calculate_score(self, y_true: np.ndarray, y_pred: np.ndarray) -> float:
        """
        Args:
            y_true: np.ndarray
            y_pred: np.ndarray
        Returns:
            recall: float
        """
        try:
            logger.info("Entered the calculate_score method of the Recall class")
            recall = recall_score(y_true, y_pred)
            logger.info("The recall score value is: " + str(recall))
            return recall
        except Exception as e:
            logger.error(
                "Exception occurred in calculate_score method of the Recall class. Exception message: " + str(e)
            )
            raise e


class F1Score(BinaryClassificationEvaluation):
    """
    Evaluation strategy that uses F1 Score for binary classification
    """
    def calculate_score(self, y_true: np.ndarray, y_pred: np.ndarray) -> float:
        """
        Args:
            y_true: np.ndarray
            y_pred: np.ndarray
        Returns:
            f1_score: float
        """
        try:
            logger.info("Entered the calculate_score method of the F1Score class")
            f1 = f1_score(y_true, y_pred)
            logger.info("The F1 score value is: " + str(f1))
            return f1
        except Exception as e:
            logger.error(
                "Exception occurred in calculate_score method of the F1Score class. Exception message: " + str(e)
            )
            raise e
