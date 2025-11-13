from pydantic import BaseModel, Field
from typing import Dict

class PredictionResponse(BaseModel):
    predicted_category: str = Field(..., description = "The predicted insurance premium category", example ="High")
    confidence: float = Field(..., description="Model's confidence score for the predicted class (range : 0 to 1)", example="0.5436")
    class_probabilities: Dict[str, float] = Field(
        ..., 
        description = "Probability distribution across all the possible classe",
        example= {"low":0.01, "medium":0.15, "High": 0.84}
    )