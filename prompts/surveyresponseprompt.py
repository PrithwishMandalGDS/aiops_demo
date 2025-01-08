################################################### Survey Response Quality Details ############################################################
survey_prompt =  """
\n\nHuman: From the given source of context, evaluate the coverage of information in each column. The provided context contains details regarding the Survey that was published to gather information for multiple applications for Discovery and Assessment purpose. Your job is to provide the coverage of percentage of data in each column present in the context. If the value for any cell is empty, consider it as a blank value. Generate response in an HTML tabular format with the columns - Column Name, Coverage Percentage, Missing Values Count (Application Names), Survey Response Quality. According to coverage percentage, the 'Survey Response Quality' should be evaluated as below:
1. If the coverage percentage is between 80 - 100 percent, then the 'Survey Response Quality' is Green.
2. If the coverage percentage is between 60 - 80 percent, then the 'Survey Response Quality' is Amber.
3. If the coverage percentage is below 60 percent, then the 'Survey Response Quality' is Red.
 
Context is contained in <context> tags below.
 
<context>
{context}
</context>
 
{question}
 
Assistant:"""
 
survey_question = "List down the percentage coverage for each column present in the context provided. Also, mention in the brackets how many entries are missing along with the names of the applications missing the information for that column. Provide 'Survey Response Quality' also for each column."
survey_input_file = "App-Inventory_v1.csv"
survey_vector_db_name = "faiss_db_survey"
survey_output_spreadsheet = "App-Survey-Response-Quality.xlsx"
survey_output_agent_spreadsheet = "App-Survey-Response-Quality_agent.xlsx"