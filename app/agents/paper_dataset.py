# The Dataset Agent extracts all the information related to the datasets used in the research paper, including
# dataset characteristics, preprocessing, splits, and usage.
from pathlib import Path
from langchain_core.prompts import PromptTemplate
from app.schemas.papaer_dataset_schema import Dataset
from app.schemas.paper_reader_schema import PaperDocument
from app.utils.utils import _prepare_input

class PaperDatasetAgent():
    def __init__(self, llm):
        path = Path("app/prompts/paper_dataset_prompt.txt")
        self.prompt = PromptTemplate.from_file(path)
        self.llm = llm
        self.structured_llm = self.llm.with_structured_output(Dataset)
        self.chain = self.prompt | self.structured_llm

    def read(self, document: PaperDocument) -> Dataset:
        prepared_input = _prepare_input(document)
        paper_dataset = self.chain.invoke(prepared_input)
        return paper_dataset