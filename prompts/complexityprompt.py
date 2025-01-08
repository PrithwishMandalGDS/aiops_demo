########################################### Complexity Inputs and Prompts Details  ############################################################
complexity_prompt = """
\n\nHuman: I'm going to give you a excel sheet in the context. Then I'm going to ask you a question about it. Document contains details about multiple applications. Details such as Application Name, Application Type, Operating System, Database Stack,No of Env,Application Dependency etc. are provided. Consider first row in the excel as the column name. Generate response in an HTML tabular format with the columns - Application Name, score_os,score_e,Application Dependency, max_val ,Complexity. Evaluate the complexity against each of the row based on the  value of max_val where max_val = (score_os + score_e + Application Dependency) .To get  the value for score_os , Application Dependency and score_e please follow the below rules and exexute it for each of the row:

When the 'Operating System' in ["AS400"], set 5 to score_os.
When the 'Operating System' in ["Ubuntu 16.04", "Ubuntu 14.04", "RHEL 8", "RHEL 9", "RHEL 7" "Ubuntu 20.04"], set 1 to score_os.
When the value for 'No of Env' is equal to 1, , then set score_e = 1 .
When the value for 'No of Env' is in  [2,3,4,5] , then set score_e = 3.
When the value for 'No of Env' is greater than 5, then set score_e = 5.
When the value for  'Application Dependency' is less than or equal to 5, then set score_d = 1 .
When the value for 'Application Dependency' is  greater than or eqaul to 6  but less than or equal to 10, then set score_d = 3.
When the value for 'Application Dependency' is greater than or equal to 11,then set score_d = 5.
When max_val is less than or equal  to 5, assign  Complexity as 'Simple'.
When max_val is greater than 5 but less than or equal to 10, assign  Complexity as 'Medium'.
When max_val is  greater than or equal to 11, assign  Complexity as 'Complex'.

**Provide the result in HTML table format**.

Context is contained in <context> tags below.

<context>
{context}
</context>

{question}

Assistant:"""

complexity_question = "Provide Complexity  for all the applications in the provided context."
complexity_input_file = "App-Inventory_v1.csv"
complexity_output_spreadsheet = "App-Complexity-Analysis.xlsx"
complexity_output_spreadsheet_agent = "App-Complexity-Analysis_agent.xlsx"
