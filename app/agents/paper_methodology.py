from pathlib import Path
from langchain_core.prompts import PromptTemplate
from app.schemas.paper_methodology_schema import methodology
from app.schemas.paper_reader_schema import PaperDocument
from app.utils.utils import _prepare_input


class PaperMethodologyAgent():
    def __init__(self, llm):
        prompt_path = Path("app/prompts/paper_methodology_prompt.txt")
        self.prompt = PromptTemplate.from_file(prompt_path)
        self.llm = llm
        self.structured_llm = self.llm.with_structured_output(methodology)
        self.chain = self.prompt | self.structured_llm

    def read(self, document: PaperDocument) -> methodology:
        prepared_input = _prepare_input(document)
        methodology_document = self.chain.invoke(prepared_input)
        return methodology_document
