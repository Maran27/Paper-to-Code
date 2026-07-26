# The Dataset Agent extracts all the information related to the datasets used in the research paper, including
# dataset characteristics, preprocessing, splits, and usage.
from pathlib import Path
from langchain_core.prompts import PromptTemplate
from app.schemas.paper_hyperparameter_schema import Hyperparameters
from app.schemas.paper_reader_schema import PaperDocument
from app.utils.utils import _prepare_input

class PaperHyperparametrersAgent():
    def __init__(self, llm):
        path = Path("app/prompts/paper_hyperparameter_prompt.txt")
        self.prompt = PromptTemplate.from_file(path)
        self.llm = llm
        self.structured_llm = self.llm.with_structured_output(Hyperparameters)
        self.chain = self.prompt | self.structured_llm

    def read(self, document: PaperDocument) -> Hyperparameters:
        prepared_input = _prepare_input(document)
        paper_hyperparameters = self.chain.invoke(prepared_input)
        return paper_hyperparameters