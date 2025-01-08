import chromadb
from chromadb.utils import embedding_functions

def initialize_chroma():
    CHROMA_DB_AIOPS_INVENTORY_PATH = "tmp/chromadb/aiops"
    CHROMA_COLLECTION = "autogen-docs"

    aiops_chroma_client = chromadb.PersistentClient(path=CHROMA_DB_AIOPS_INVENTORY_PATH)

    AIOPS_collection = aiops_chroma_client.get_or_create_collection(name=CHROMA_COLLECTION)

    return aiops_chroma_client, AIOPS_collection, CHROMA_DB_AIOPS_INVENTORY_PATH, CHROMA_COLLECTION

def initialize_chroma_advisor():
    CHROMA_DB_AIOPS_INVENTORY_PATH_ADVISOR = "tmp/chromadb/advisor"
    CHROMA_COLLECTION = "autogen-docs"

    aiops_chroma_client = chromadb.PersistentClient(path=CHROMA_DB_AIOPS_INVENTORY_PATH_ADVISOR)

    AIOPS_collection = aiops_chroma_client.get_or_create_collection(name=CHROMA_COLLECTION)

    return aiops_chroma_client, AIOPS_collection, CHROMA_DB_AIOPS_INVENTORY_PATH_ADVISOR, CHROMA_COLLECTION

def initialize_chroma_advisor_solution():
    CHROMA_DB_AIOPS_INVENTORY_PATH_ADVISOR_SOL = "tmp/chromadb/advsol"
    CHROMA_COLLECTION = "autogen-docs"

    aiops_chroma_client = chromadb.PersistentClient(path=CHROMA_DB_AIOPS_INVENTORY_PATH_ADVISOR_SOL)

    AIOPS_collection = aiops_chroma_client.get_or_create_collection(name=CHROMA_COLLECTION)

    return aiops_chroma_client, AIOPS_collection, CHROMA_DB_AIOPS_INVENTORY_PATH_ADVISOR_SOL, CHROMA_COLLECTION

def initialize_openai_embedding_function():
    OPENAI_EMBEDDING_MODEL = 'text-embedding-ada-002'
    OPENAI_API_KEY = 'dFndVNaSSIzadHvG0LFCkIA7GIuQaeiz'
    OPENAI_API_BASE = 'https://eyq-incubator.asiapac.fabric.ey.com/eyq/as/api'
    OPENAI_API_TYPE = 'azure'
    OPENAI_API_VERSION = '2023-05-15'

    openai_ef = embedding_functions.OpenAIEmbeddingFunction(
        model_name=OPENAI_EMBEDDING_MODEL,
        api_key=OPENAI_API_KEY,
        api_base=OPENAI_API_BASE,
        api_type=OPENAI_API_TYPE,
        api_version=OPENAI_API_VERSION
    )

    return openai_ef
