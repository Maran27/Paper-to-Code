from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
import os

load_dotenv()
os.environ["OPENROUTER_API_KEY"] = os.getenv("OPENROUTER_API_KEY")
def get_llm():
    """
    Returns an instance of the LLM (Language Model) to be used for processing and generating summaries.
    Returns:
        LLM: An instance of the LLM.
    """
    # llm = init_chat_model(
    #     model="gemma3:1b",
    #     model_provider="ollama",
    #     temperature=0.2
    # )
    llm = init_chat_model(
        model="openrouter/free",
        model_provider="openrouter",
        temperature=0.2
    )
    return llm