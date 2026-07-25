from app.schemas.paper_reader_schema import PaperDocument
def _prepare_input(document: PaperDocument) -> dict[str,str]:
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