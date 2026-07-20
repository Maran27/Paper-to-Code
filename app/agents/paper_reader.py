from pathlib import Path
from pydoc import doc
from app.schemas.paper_reader_schema import PaperDocument, PaperMetaData, Page
from app.services.text_cleaner import TextCleaner
import pymupdf 

class PaperReaderAgent():
    def __init__(self):
        self.cleaner = TextCleaner()
    def read(self, paper_path: str) -> PaperDocument:
        """
        Reads a research paper from the given path and extracts relevant information.
        Args:
            paper_path (str): The path to the research paper file.
        Returns:
            PaperDocument: The extracted information about the research paper.
        """
        self._validate_pdf(paper_path)
        pages = self._extract_pages(paper_path)
        document = self._create_document(paper_path, pages)
        return document
    def _validate_pdf(self, paper_path: str) -> bool:
        """
        Validates the PDF file to ensure it is a valid research paper.
        Returns:
            bool: True if the PDF is valid, False otherwise.
        """
        path = Path(paper_path)
        if path.exists():
            print(f"The file {path} exists.")
            if path.suffix.lower() == ".pdf":
                print(f"The file {path} is a valid PDF.")
            else:
                raise ValueError(f"The file {path} is not a valid PDF.")
        else:
            raise FileNotFoundError(f"The file {path} does not exist.")
        try:
            doc = pymupdf.open(path)
            if doc.is_pdf:
                print(f"The file {path} is a valid PDF.")
                return True
        except Exception as e:
            raise ValueError(f"An error occurred while validating the PDF: {e}")
        
    def _extract_pages(self, paper_path: str) -> list[Page]:
        """
        Extracts the pages from the research paper and their content.
        Returns:
            list[Page]: A list of Page objects containing page number, content, and word count.
        """
        try:
            with pymupdf.open(paper_path) as doc:
                pages = []
                for page_number in range(len(doc)):
                    page = doc[page_number]
                    content = page.get_text()
                    content = self.cleaner.clean_text(content)
                    word_count = len(content.split())
                    page_obj = Page(page_number=page_number + 1, content=content, word_count=word_count)
                    pages.append(page_obj)
                return pages
        except Exception as e:
            raise ValueError(f"An error occurred while extracting pages: {e}")
    def _create_document(self, paper_path: str, pages: list) -> PaperDocument:
        """
        Creates a PaperDocument object containing metadata and pages of the research paper.
        Returns:
            PaperDocument: The constructed PaperDocument object.
        """
        try:
            path = Path(paper_path)
            metadata = PaperMetaData(
                file_name=path.name,
                page_count=len(pages)
            )
            document = PaperDocument(metadata=metadata, pages=pages)
            return document
        except Exception as e:
            raise ValueError(f"An error occurred while creating the document: {e}")
