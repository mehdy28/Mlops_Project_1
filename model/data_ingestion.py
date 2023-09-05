import pandas as pd
from log import logger
import logging

class IngestData:
    """
    Data ingestion class which ingests data from the source and returns a DataFrame.
    """

    def __init__(self, csv_path) -> None:
        """Initialize the data ingestion class with the CSV file path."""
        self.csv_path = csv_path

    def get_data(self) -> pd.DataFrame:
        try:
            df = pd.read_csv(self.csv_path)
            logger.info("Data ingestion successful.")
            logging.getLogger().handlers[0].flush()
            return df
        except Exception as e:
            logger.error(f"Error during data ingestion: {e}")
            logging.getLogger().handlers[0].flush()
            raise e