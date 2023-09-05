from abc import ABC, abstractmethod
from typing import Union, Tuple
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from log import logger


class DataStrategy(ABC):
    """
    Abstract Class defining strategy for handling data
    """

    @abstractmethod
    def handle_data(self, data: pd.DataFrame) -> Union[pd.DataFrame, pd.Series]:
        pass
    
class DataPreprocessStrategy(DataStrategy):
    """
    Data preprocessing strategy which preprocesses the data.
    """
    def handle_data(self, data: pd.DataFrame) -> pd.DataFrame:
        """
        Removes columns which are not required, fills missing values with median average values, and converts the data type to float.
        """
        try:
            # List of columns to drop
            columns_to_drop = ['Employee_Name', 'EmpID', 'ManagerName', 'ManagerID', 'DateofHire', 'DateofTermination','LastPerformanceReview_Date','DOB']
            cleaned_df  = data.drop(columns=columns_to_drop, axis=1)
            logger.info("Colum dropping successful.")
        except Exception as e:
            logger.error(f"Error during column dropping: {e}")
            raise e
        try:
            # Identify categorical columns
            categorical_columns = cleaned_df.select_dtypes(include=['object']).columns

            # Create a LabelEncoder instance
            label_encoder = LabelEncoder()

            # Apply label encoding to each categorical column
            for column in categorical_columns:
                cleaned_df[column] = label_encoder.fit_transform(cleaned_df[column])
            logger.info("Label encoding successful.")
        except Exception as e:
            logger.error(f"Error during label encoding: {e}")
            raise e
        return cleaned_df
    
class DataDivideStrategy(DataStrategy):
    """
    Data dividing strategy which divides the data into train and test data.
    """

    def handle_data(self, data: pd.DataFrame) -> Tuple[pd.DataFrame, pd.DataFrame, pd.Series, pd.Series]:
        """
        Divides the data into train and test data.
        """
        try:
            X = data.drop("Termd", axis=1)
            y = data["Termd"]
            X_train, X_test, y_train, y_test = train_test_split(
                X, y, test_size=0.2, random_state=42
            )
            return X_train, X_test, y_train, y_test
        except Exception as e:
            logger.error(e)
            raise e
class DataCleaning:
    """
    Data cleaning class which preprocesses the data and divides it into train and test data.
    """

    def __init__(self, data: pd.DataFrame, strategy: DataStrategy) -> None:
        """Initializes the DataCleaning class with a specific strategy."""
        self.df = data
        self.strategy = strategy

    def handle_data(self) -> Union[pd.DataFrame, pd.Series]:
        """Handle data based on the provided strategy"""
        return self.strategy.handle_data(self.df)