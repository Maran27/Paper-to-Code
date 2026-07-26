from pydantic import BaseModel, Field

class Metrics(BaseModel):
    name: str
    purpose: str

class Ablation_Studies(BaseModel):
    component_removed: str
    impact: str

class Results(BaseModel):
    model: str
    dataset: str | None
    metric: str
    score: str | float

class BaseLine(BaseModel):
    name: str
    description: str

class Comparisons(BaseModel):
    compared_with: str
    outcome: str

class Evaluation(BaseModel):
    metrics: list[Metrics]
    baselines: list[BaseLine]
    results: list[Results]
    comparisons: list[Comparisons]
    ablation_studies: list[Ablation_Studies]
    conclusions: list[str]
