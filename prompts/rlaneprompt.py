########################################### R-Lane Inputs and Prompts Details  ############################################################
rlane_prompt = """
\n\nHuman: I'm going to give you a excel sheet in the context. Then I'm going to ask you a question about it. Document contains details about multiple applications. Details such as Application Name, Application Type, Operating System, Database Stack, etc. are provided. Consider first row in the excel as the column name. Generate response in a HTML tabular format with the columns - Application Name, Infra R-Lane, Infra R-Lane Rationale, App R-Lane , App R-Lane Rationale, Final R-Lane.
Evaluate Infra R-Lane and App R-Lane for each of the application based on the below criteria only. If any of the data is missing, consider the next criteria.

Consider below criteria for evaluating Infra R-Lane:
When 'Operating System' in ["AS400"], then set Infra R-Lane as Retire and skip the below  conditions.
When 'Operating System' in ["Ubuntu 14.04", "Ubuntu 16.04", "RHEL 7", "RHEL 8"], then set Infra R-Lane as Replatform and skip the below  conditions.
When 'Operating System' in ['RHEL 9', 'Ubuntu 20.04'], then set Infra R-Lane as Rehost and skip the below conditions.

Consider below criteria for evaluating App R-Lane:
When 'Database versions' in ["Oracle 10", "Oracle 12"] AND 'Application Tech Stack' in ["JDK 1.7"], then set App R-Lane as Refactor and skip the below  conditions.
When 'Database versions' in ["Oracle 10"], then set App R-Lane as Refactor and skip the below  conditions.
When 'Database versions' in ["Oracle 12"], then set App R-Lane as Replatform and skip the below  conditions.
When 'Application Tech Stack' in ["JDK 1.7"], then set App R-Lane as Refactor and skip the below  conditions.
When 'Database versions' in ["Oracle 19"] AND 'Application Tech Stack' in ["JAVA 8", "JAVA 11"], then set App R-Lane as Replatform and skip the below  conditions.
When 'Database versions' in ["Oracle 19"] AND 'Application Tech Stack' in ["JAVA 17", "JDK 1.8"], then set App R-Lane as Rehost and skip the below  conditions.

Provide rationale for Infra R-Lane and App R-Lane as below:
If latest Operating System or Database version or Application tech stack is found in the document such as "Ubuntu 20.04" or "Oracle 19", rationale should be "Latest tech stack for lift and shift" along with the Tech Stack details for the latest tech stack only. But in case of Replatform R-Lane evaluation where latest tech stack might be present in the evaluation logic, the rationale should be "Tech Stack running EOS/EOL" along with the old Tech stack details only.
If Operating System or Database version or Application tech stack running End of Life/End of Support is found in the document such as "Ubuntu 16.04" or "Java 11" which is not the oldest one, rationale should be "Tech Stack running EOS/EOL" along with the Tech Stack details.
If oldest Operating System or Database version or Application tech stack is found in the document such as "RHEL 7" or "Oracle 10", rationale should be "Tech Stack needs significant upgrade resuting in code change" along with the Tech Stack details.

Final R-Lane should be evaluated based on Infra R-Lane and App R-Lane. The criteria to evaluate the Final R-Lane is below. Once the criteria is met, do not evaluate the remaining conditions.
1. If any one of the Infra R-Lane or App R-Lane is Retire, then the Final R-Lane should be Retire and skip the below conditions.
2. If any one of the Infra R-Lane or App R-Lane is Refactor, then the Final R-Lane should be Refactor and skip the below conditions.
3. If any one of the Infra R-Lane or App R-Lane is Replatform, then the Final R-Lane should be Replatform and skip the below conditions.
4. If both the Infra R-Lane and App R-Lane are Rehost, then the Final R-Lane should be Rehost.

**Provide the result in HTML table format**.

Context is contained in <context> tags below.

<context>
{context}
</context>

{question}

Assistant:"""

rlane_question = "Provide R-Lane for all the applications in the provided context."
rlane_input_file = "App-Inventory_v1.csv"
rlane_output_spreadsheet = "App-RLane-Analysis.xlsx"
rlane_output_spreadsheet_agent = "App-RLane-Analysis_agent.xlsx"