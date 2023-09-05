import pandas as pd
from model.model_evaluation import (
    Accuracy,
    Precision,
    Recall,
    F1Score
)
from zenml import step
from sklearn.base import ClassifierMixin
from typing_extensions import Annotated 
from typing import Tuple



@step
def model_evaluation(
    model:ClassifierMixin, x_test: pd.DataFrame, y_test: pd.Series
) -> Tuple[
    Annotated[float, "accuracy"],
    Annotated[float, "precision"],
    Annotated[float, "recall"],
    Annotated[float, "f_1"],
]:
    """
    Evaluate a binary classification model using specified evaluation strategies.

    Args:
        model: Binary classification model (e.g., RandomForestClassifier).
        x_test: Test features (pd.DataFrame).
        y_test: True labels (pd.Series).
        
    Returns:
        evaluation_results: A dictionary containing metric names as keys and their scores as values.
    """
    accuracy = 0
    precision = 0
    recall = 0
    f_1 = 0

    # Create instances of evaluation strategies
    accuracy_strategy = Accuracy()
    precision_strategy = Precision()
    recall_strategy = Recall()
    f1_score_strategy = F1Score()

    # Predict using the model
    y_pred = model.predict(x_test)

    # Calculate and store the evaluation metrics
    accuracy = accuracy_strategy.calculate_score(y_test.values, y_pred)
    precision = precision_strategy.calculate_score(y_test.values, y_pred)
    recall = recall_strategy.calculate_score(y_test.values, y_pred)
    f_1 = f1_score_strategy.calculate_score(y_test.values, y_pred)

    return accuracy ,precision , recall , f_1


