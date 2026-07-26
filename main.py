from app.agents.paper_reader import PaperReaderAgent
from app.agents.paper_summary import PaperSummaryAgent
from app.agents.paper_methodology import PaperMethodologyAgent
from app.agents.paper_dataset import PaperDatasetAgent
from app.agents.paper_hyperparameter import PaperHyperparametrersAgent
from app.agents.paper_evaluation import PaperEvaluationAgent
from app.config.llm import get_llm
from pprint import pprint

def main():
    """
    Main function to read a research paper, generate a summary, and print the summary.
    """
    llm = get_llm()
    reader_agent = PaperReaderAgent()
    summary_agent = PaperSummaryAgent(llm)
    methodology_agent = PaperMethodologyAgent(llm)
    dataset_agent = PaperDatasetAgent(llm)
    hyperparameters_agent = PaperHyperparametrersAgent(llm)
    evaluation_agent = PaperEvaluationAgent(llm)

    paper_document = reader_agent.read("data/papers/1909.13522v1.pdf")

    paper_summary = summary_agent.read(paper_document)
    pprint(paper_summary.model_dump())

    paper_methodology = methodology_agent.read(paper_document)
    pprint(paper_methodology.model_dump())

    paper_dataset = dataset_agent.read(paper_document)
    pprint(paper_dataset.model_dump())

    paper_hyperparameters = hyperparameters_agent.read(paper_document)
    pprint(paper_hyperparameters.model_dump())

    paper_evaluation = evaluation_agent.read(paper_document)
    pprint(paper_evaluation.model_dump())

if __name__ == "__main__":
    main()