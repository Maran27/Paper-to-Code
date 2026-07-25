from pydantic import BaseModel, Field

class MethodologyComponent(BaseModel):
    name: str
    purpose: str

class MethodologyAlgorithm(BaseModel):
    name: str
    purpose: str

class MethodologyMaths(BaseModel):
    equation: str
    description: str

class methodology(BaseModel):
    """
    Represents the methodology extracted from a research paper.
    This schema captures the information required to understand
    and reproduce the proposed approach.
    """
    overview: str
    pipeline_steps: list[str]
    implementation_steps: list[str]
    model_architecture: str
    components: list[MethodologyComponent]
    algorithms: list[MethodologyAlgorithm]
    training_procedure: str
    inference_procedure: str
    mathematical_formulations: list[MethodologyMaths]
    novel_techniques: list[str]
    assumptions: list[str]
    limitations: list[str]

