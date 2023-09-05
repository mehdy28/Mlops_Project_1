from log import logger
import pandas as pd
from model.data_cleaning import DataCleaning, DataPreprocessStrategy


def get_data_for_test():
    try:
        df = pd.read_csv("./data/raw_data.csv")
        df = df.sample(n=30)
        preprocess_strategy = DataPreprocessStrategy()
        data_cleaning = DataCleaning(df, preprocess_strategy)
        df = data_cleaning.handle_data()
        df.drop(["Termd"], axis=1, inplace=True)
        result = df.to_json(orient="split")
        return result
    except Exception as e:
        logger.error(e)
        raise e
