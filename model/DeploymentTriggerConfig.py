from zenml.steps import BaseParameters



class DeploymentTriggerConfig(BaseParameters):
    """Parameters that are used to trigger the deployment"""

    min_f1: float = 0.9