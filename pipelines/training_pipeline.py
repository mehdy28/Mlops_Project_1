from steps.data_ingestion import ingest_data
from steps.data_cleaning import clean_data
from steps.model_development import execute_model_tuning
from steps.model_evaluation import model_evaluation
from zenml import pipeline

@pipeline(enable_cache=True)
def train_pipline(data_path:str):
    df = ingest_data(data_path)
    x_train, x_test, y_train, y_test = clean_data(df)
    model = execute_model_tuning(x_train, x_test, y_train, y_test)
    accuracy ,precision , recall , f_1 = model_evaluation(model,x_test,y_test)
    