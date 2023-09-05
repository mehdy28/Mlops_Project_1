from model.DeploymentTriggerConfig import DeploymentTriggerConfig
from zenml import step

@step
def deployment_trigger(
    f1: float,
    config: DeploymentTriggerConfig,
) -> bool:
    """Implements a simple model deployment trigger that looks at the
    input model f1 and decides if it is good enough to deploy"""

    return f1 > config.min_f1