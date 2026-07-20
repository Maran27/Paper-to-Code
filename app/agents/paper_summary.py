from app.schemas.paper_summary_schema import PaperSummary
from pathlib import Path
from langchain_core.prompts import PromptTemplate
from app.schemas.paper_reader_schema import PaperDocument

# Langchain gives us the pipeline work that proces our request using the llm and provide us an output.
# | operator take the output from the left and feed it to the right as the input.
# For our current project, your approach is perfectly fine, because each agent has a single responsibility and a single output schema.
# If we were building a larger framework where one class handled multiple schemas, we'd probably move that responsibility closer to the chain.
# Always Prompt | LLM | Structured Output
# That's low coupling and high cohesion, which are two design principles you'll hear a lot in software engineering.
# Having the dictionary type retrun from the function will help to keep the code more flexible and easier to maintain. It allows for easier integration with other components of the system, as well as easier testing and debugging. Additionally, it allows for more flexibility in terms of the output format, as the dictionary can be easily converted to other formats if needed.
class PaperSummaryAgent():
    def __init__(self, llm):
        # self.prompt = prompt
        path = Path("app/prompts/paper_summary_prompt.txt")
        self.prompt_template = PromptTemplate.from_file(path)
        self.llm = llm
        self.structured_llm = self.llm.with_structured_output(PaperSummary)
        self.chain = self.prompt_template | self.structured_llm


    def read(self, document: PaperDocument) -> PaperSummary:
        """
        Reads the input document text and prepares it and passes it to the LLM for processing and generating a summary.
        Args:
            document (PaperDocument): The input document containing the research paper's content.
        returns:
            PaperSummary: An instance of PaperSummary containing the generated summary and other relevant information.
        """
        prepared_input = self._prepare_input(document)
        summary_document = self.chain.invoke(prepared_input)
        return summary_document


    def _prepare_input(self, document: PaperDocument) -> dict[str,str]:
        """
        Takes the document as input and combines all the content in all the pages into a single string
        Args:
            document (PaperDocument): The input document containing the research paper's content.
        Returns:
            dict[str, str]: A dictionary containing the combined content of the research paper.
        """
        # Combine the content of all pages into a single string
        combined_content = "\n".join(page.content for page in document.pages)
        return {"text": combined_content}


