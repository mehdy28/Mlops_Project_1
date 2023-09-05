from zenml import step
from zenml.integrations.mlflow.services import MLFlowDeploymentService
from typing import Union
import pandas as pd
import numpy as np
import json


@step
def predictor(
    service: MLFlowDeploymentService,
    data: Union[pd.DataFrame, str],
) -> np.ndarray:
    """Run an inference request against a prediction service"""

    service.start(timeout=10)  # should be a NOP if already started
    
    if isinstance(data, str):
        data = json.loads(data)
        data = pd.DataFrame(data)  # Convert the JSON data to a DataFrame
        
    columns_for_df = [
        "MarriedID",
        "MaritalStatusID",
        "GenderID",
        "EmpStatusID",
        "DeptID",
        "PerfScoreID",
        "FromDiversityJobFairID",
        "Salary",
        "PositionID",
        "Position",
        "State",
        "Zip",
        "Sex",
        "MaritalDesc",
        "CitizenDesc",
        "HispanicLatino",
        "RaceDesc",
        "TermReason",
        "EmploymentStatus",
        "Department",
        "RecruitmentSource",
        "PerformanceScore",
        "EngagementSurvey",
        "EmpSatisfaction",
        "SpecialProjectsCount",
        "DaysLateLast30",
        "Absences",
    ]
    
    # Reorder the columns to match the expected format
    df = data[columns_for_df]
    
    # Convert DataFrame to numpy array for prediction
    prediction = service.predict(df.values)
    
    return prediction
