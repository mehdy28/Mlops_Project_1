from zenml.client import Client
from pipelines.training_pipeline import train_pipline



if __name__=="__main__":
    print(Client().active_stack.experiment_tracker.get_tracking_uri())
    train_pipline("data/raw_data.csv")
