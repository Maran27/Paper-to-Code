from app.agents.paper_reader import PaperReaderAgent
from app.agents.paper_summary import PaperSummaryAgent
from app.config.llm import get_llm

def main():
    """
    Main function to read a research paper, generate a summary, and print the summary.
    """
    reader = PaperReaderAgent()

    llm = get_llm()
    summary_agent = PaperSummaryAgent(llm)

    paper_document = reader.read("data/papers/1909.13522v1.pdf")

    paper_summary = summary_agent.read(paper_document)

    print(paper_summary)

    from pprint import pprint

    pprint(paper_summary.model_dump())

    # print(paper)
    # print("File:", paper.metadata.file_name)
    # print("Pages:", paper.metadata.page_count)

    # print()

    # print(paper.pages[0].content[:500])

    # print(f"File Name: {paper.metadata.file_name}")
    # print(f"Page Count: {paper.metadata.page_count}")

    # print("-" * 50)

    # for page in paper.pages:
    #     print(f"Page {page.page_number}")
    #     print(f"Words: {page.word_count}")
    #     print(f"Characters: {len(page.content)}")
    #     print(page.content[:100])
    #     print("-" * 50)

if __name__ == "__main__":
    main()