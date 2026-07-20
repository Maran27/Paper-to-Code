from pydantic import BaseModel, Field

class Page(BaseModel):
    """Tells about the page and its content from the research paper"""
    page_number: int
    content: str
    word_count: int

class PaperMetaData(BaseModel):
    """Tells about the research paper"""
    file_name: str
    page_count: int

class PaperDocument(BaseModel):
    """Tells about the research paper and its content"""
    metadata: PaperMetaData
    pages: list[Page] = Field(default_factory=list)