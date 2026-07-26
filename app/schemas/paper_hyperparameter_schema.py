from pydantic import BaseModel, Field

class Optimizer(BaseModel):
    name: str
    purpose: str
    parameters: dict[str,str]

class LossFunction(BaseModel):
    name: str
    purpose: str
    formula: str

class LearningRate(BaseModel):
    initial: str
    schedule: str

class Scheduler(BaseModel):
    name: str
    description: str

class Regularization(BaseModel):
    name: str
    description: str

class Hyperparameters(BaseModel):
    optimizer: list[Optimizer]
    lossfunction: list[LossFunction]
    learning_rate: LearningRate
    batch_size: int | None
    epochs: int | None
    weight_decay: str | None
    scheduler: Scheduler | None
    regularization: Regularization | None
    initialization: str | None
