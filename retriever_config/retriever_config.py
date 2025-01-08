from llm_config.llm_config import initialize_llm_config
from chromaDB.aiops_chroma_client import initialize_chroma, initialize_openai_embedding_function, initialize_chroma_advisor, initialize_chroma_advisor_solution
from autogen.agentchat.contrib.vectordb.chromadb import ChromaVectorDB

def initialize_aiops_dataframe_config(chunk_token_size, docs_path, n_results, get_or_create, overwrite, update_context):
    aiops_chroma_client, AIOPS_collection, CHROMA_DB_AIOPS_INVENTORY_PATH, CHROMA_COLLECTION = initialize_chroma()
    AIOPS_collection = aiops_chroma_client.get_or_create_collection(name=CHROMA_COLLECTION)
    openai_ef = initialize_openai_embedding_function()
    aiops_vector_db = ChromaVectorDB(path=CHROMA_DB_AIOPS_INVENTORY_PATH, embedding_function = openai_ef)
    custom_timeout = 600
    custom_temperature = 0.9
    llm_config = initialize_llm_config(timeout=custom_timeout, temperature=custom_temperature)
    aiops_config = {
        "task": "qa",
        "model": llm_config['config_list'][0]['model'],
        "update_context": update_context,
        "chunk_token_size": chunk_token_size,
        "n_results": n_results,
        "docs_path": docs_path,
        "get_or_create": get_or_create,
        "overwrite": overwrite,
        "vector_db": aiops_vector_db,
        "collection_name": CHROMA_COLLECTION,
        "embedding_function": openai_ef
    }
    return aiops_config

def initialize_aiops_advisor_dataframe_config(chunk_token_size, docs_path, n_results, get_or_create, overwrite, update_context):
    aiops_chroma_adv_client, AIOPS_collection_adv, CHROMA_DB_AIOPS_INVENTORY_PATH_ADVISOR, CHROMA_COLLECTION = initialize_chroma_advisor()
    AIOPS_collection_adv = aiops_chroma_adv_client.get_or_create_collection(name=CHROMA_COLLECTION)
    openai_ef = initialize_openai_embedding_function()
    aiops_vector_db = ChromaVectorDB(path=CHROMA_DB_AIOPS_INVENTORY_PATH_ADVISOR, embedding_function = openai_ef)
    custom_timeout = 600
    custom_temperature = 0.9
    llm_config = initialize_llm_config(timeout=custom_timeout, temperature=custom_temperature)
    aiops_config_advisor = {
        "task": "qa",
        "model": llm_config['config_list'][0]['model'],
        "update_context": update_context,
        "chunk_token_size": chunk_token_size,
        "n_results": n_results,
        "docs_path": docs_path,
        "get_or_create": get_or_create,
        "overwrite": overwrite,
        "vector_db": aiops_vector_db,
        "collection_name": CHROMA_COLLECTION,
        "embedding_function": openai_ef
    }
    return aiops_config_advisor

def initialize_aiops_advisor_solution_config(chunk_token_size, docs_path_sol, n_results, get_or_create, overwrite, update_context):
    aiops_chroma_sol_client, AIOPS_collection_sol, CHROMA_DB_AIOPS_INVENTORY_PATH_ADVISOR_SOL, CHROMA_COLLECTION = initialize_chroma_advisor_solution()
    AIOPS_collection_sol = aiops_chroma_sol_client.get_or_create_collection(name=CHROMA_COLLECTION)
    openai_ef = initialize_openai_embedding_function()
    aiops_vector_db = ChromaVectorDB(path=CHROMA_DB_AIOPS_INVENTORY_PATH_ADVISOR_SOL, embedding_function = openai_ef)
    custom_timeout = 600
    custom_temperature = 0.9
    llm_config = initialize_llm_config(timeout=custom_timeout, temperature=custom_temperature)
    aiops_config_advisor_sol = {
        "task": "qa",
        "model": llm_config['config_list'][0]['model'],
        "update_context": update_context,
        "chunk_token_size": chunk_token_size,
        "n_results": n_results,
        "docs_path": docs_path_sol,
        "get_or_create": get_or_create,
        "overwrite": overwrite,
        "vector_db": aiops_vector_db,
        "collection_name": CHROMA_COLLECTION,
        "embedding_function": openai_ef
    }
    return aiops_config_advisor_sol