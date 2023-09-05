import pandas as pd
from log import logger
from model.data_ingestion import IngestData
import logging
from zenml import step

@step
def ingest_data(csv_path: str) -> pd.DataFrame:
    """
    Args:
        csv_path (str): Path to the CSV file.
    Returns:
        df: pd.DataFrame
    """
    try:
        ingest_data_obj = IngestData(csv_path)
        df = ingest_data_obj.get_data()
        return df
    except Exception as e:
        logger.error(f"Error during data ingestion process: {e}")
        logging.getLogger().handlers[0].flush()
        raise e