from pydantic import BaseModel, Field

class PaperSummary(BaseModel):
    """Here we generate and extract important information about the research paper"""
    title: str = Field(..., description="The title of the research paper")
    abstract: str = Field(..., description="This tells about the research paper's abstract")
    problem_statement: str = Field(..., description="This tells about the research paper's problem statement")  
    main_contribution: str = Field(..., description="This tells about the research paper's main contribution")
    summary: str = Field(..., description="This tells about the research paper's summary")
    research_domain: str = Field(..., description="This tells about the research paper's research domain")
    keywords: list[str] = Field(..., description="This tells about the research paper's keywords")