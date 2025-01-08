from autogen import Cache
import pandas as pd
import json
import ast
import re
from fuzzywuzzy import process


def process_recommendation_advisor_dtf(rag_proxy_agent, aiops_recomenndation_agent, question):
    with Cache.disk() as cache:
        aiops_recommendation_response = rag_proxy_agent.initiate_chat(
            aiops_recomenndation_agent,
            problem=question,
            n_results=1,
            message=rag_proxy_agent.message_generator,
            max_turns=1
        )

    with open("full_chat_history.txt", "w") as f1:
        f1.write(str(aiops_recommendation_response.chat_history))

    csv_content_survey_response = next((
        item['content'] for item in aiops_recommendation_response.chat_history 
        if 'aiops_adv_recomenndation_agent' in item['name']
    ), None)

    with open("dataset/agentOP/agentop.csv", "w") as f:
        if csv_content_survey_response:
            f.write(csv_content_survey_response)
    
    return csv_content_survey_response

def process_recommendation_advisor_sol(rag_proxy_agent_sol, aiops_recomenndation_agent_sol, question):
    csv_file_path = "dataset/agentOP/agentop.csv"
    df = pd.read_csv(csv_file_path, header=None, names=["id", "Problem"])
    problem_column = "Problem"
    output_path = "Reports/Report.csv"
    with Cache.disk() as cache:
        aiops_recommendation_response_sol = rag_proxy_agent_sol.initiate_chat(
            aiops_recomenndation_agent_sol,
            problem=question,
            n_results=1,
            message=rag_proxy_agent_sol.message_generator,
            max_turns=1
        )

    with open("full_chat_history_sol.txt", "w") as f1:
        f1.write(str(aiops_recommendation_response_sol.chat_history))

    f = open("problemsolution.txt", "w")
    csv_content_survey_response = next((item['content'] for item in aiops_recommendation_response_sol.chat_history if 'aiops_sol_recomenndation_agent' in item['name']), None)
    f.write(csv_content_survey_response)
    f.close()

    text_file_path = "problemsolution.txt" 
    with open(text_file_path, 'r') as file:
       content = file.read()
    pattern = r'"(.*?)" - (.*?)\n*(?=\d+\.|$)'
    matches = re.findall(pattern, content, re.DOTALL)
    problem_solution_dict = {problem.strip(): solution.strip() for problem, solution in matches}
    df["Problem"] = df["Problem"].str.strip().str.lower()
    problem_solution_dict_cleaned = {k.strip().lower(): v for k, v in problem_solution_dict.items()}

    def find_solution(problem):
        best_match, score = process.extractOne(problem, problem_solution_dict_cleaned.keys())
        if score > 80:
            return problem_solution_dict_cleaned[best_match]
        return None
    df["Solution"] = df["Problem"].apply(find_solution)
    df.to_csv(output_path, index=False)

    return csv_content_survey_response