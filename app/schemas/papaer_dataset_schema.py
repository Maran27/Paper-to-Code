from pydantic import BaseModel, Field

class Samples(BaseModel):
    name: str
    number: int
    description: str

class DatasetStatistics(BaseModel):
    total: int | None
    training: int | None
    validation: int | None
    testing: int | None

class Split(BaseModel):
    train: int | None
    validation: int | None
    test: int | None

class Preprocessing(BaseModel):
    name: str
    purpose: str

class DatasetItem(BaseModel):
    name: str
    description: str

class Dataset(BaseModel):
    dataset_used: list[DatasetItem] = Field(description="The dataset used in the paper")
    stats: DatasetStatistics
    availability: str
    split: Split
    preprocessing: list[Preprocessing] | None