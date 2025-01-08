from autogen import Agent, Cache
from Agents.chat import process_recommendation_advisor_dtf, process_recommendation_advisor_sol
from Agents.agent_configurations import aiops_avd_rag_proxy_agent, aiops_recomenndation_adv_agent, aiops_sol_rag_proxy_agent, aiops_recomenndation_sol_agent
from prompts.aiopsprompt import aiops_advisor_question_dtf, aiops_advisor_question_sol
import pandas as pd
class AdvisorAgent(Agent):
    def __init__(self, name):
        super().__init__(name=name)

    def process_data(self, data):
        if(data == "advisor"):
            print("Processing Advisor Dataframe using DTF Agent") 
            response = process_recommendation_advisor_dtf(aiops_avd_rag_proxy_agent, aiops_recomenndation_adv_agent, aiops_advisor_question_dtf)
            print("DTF Agent called Sol Agent for the response") 
            response_sol = process_recommendation_advisor_sol(aiops_sol_rag_proxy_agent, aiops_recomenndation_sol_agent, aiops_advisor_question_sol)
        return f"Responses are processed using SOL Agent"