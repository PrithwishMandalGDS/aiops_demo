from Agents.workers.worker_user_proxy_agent import AIOPSRAGProxyAgent
from Agents.workers.worker_assistant_agent import AIOPSAssistantAgent
from llm_config.llm_config import initialize_llm_config
from retriever_config.retriever_config import initialize_aiops_advisor_dataframe_config, initialize_aiops_advisor_solution_config
from prompts.aiopsprompt import aiops_advisor_agent_system_message_dtf, aiops_advisor_agent_system_message_sol

update_context = True
chunk_token_size = 6000
n_results = 5
docs_path = ["./dataset/output_advisor.csv"]
docs_path_sol = ["./dataset/agentOP/agentop.csv"]
get_or_create = True
overwrite = True
custom_timeout = 600
custom_temperature = 0.9
llm_config = initialize_llm_config(timeout=custom_timeout, temperature=custom_temperature)
aiops_dataframe_config_adv = initialize_aiops_advisor_dataframe_config(chunk_token_size, docs_path, n_results, get_or_create, overwrite, update_context)
aiops_solution_config_adv = initialize_aiops_advisor_solution_config(chunk_token_size, docs_path_sol, n_results, get_or_create, overwrite, update_context)

agent_creator_rag_dtf = AIOPSRAGProxyAgent(
    name="aiops_adv_rag_proxy_agent",
    human_input_mode="NEVER",
    llm_config=llm_config,
    retrieve_config=aiops_dataframe_config_adv,
    code_execution_config=False,
)
aiops_avd_rag_proxy_agent = agent_creator_rag_dtf.create_agent()

agent_creator_rag_sol = AIOPSRAGProxyAgent(
    name="aiops_sol_rag_proxy_agent",
    human_input_mode="NEVER",
    llm_config=llm_config,
    retrieve_config=aiops_solution_config_adv,
    code_execution_config=False,
)
aiops_sol_rag_proxy_agent = agent_creator_rag_sol.create_agent()

agent_creator_assistant_dtf = AIOPSAssistantAgent(
    name="aiops_adv_recomenndation_agent",
    system_message=aiops_advisor_agent_system_message_dtf,
    llm_config=llm_config
)
aiops_recomenndation_adv_agent = agent_creator_assistant_dtf.create_agent()

agent_creator_assistant_sol = AIOPSAssistantAgent(
    name="aiops_sol_recomenndation_agent",
    system_message=aiops_advisor_agent_system_message_sol,
    llm_config=llm_config
)
aiops_recomenndation_sol_agent = agent_creator_assistant_sol.create_agent()
