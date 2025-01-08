########################################### Move group Inputs and Prompts Details  ############################################################
movegroup_prompt = """
\n\nHuman: You will receive a spreadsheet containing details about multiple applications. The document includes information such as Application Name, Inbound Apps, Outbound Apps, etc. The first row in the Excel sheet represents the column names. Your task is to generate a response in an HTML tabular format with the columns: Move Group, Application Grouping, and Rationale.

Each row in the spreadsheet represents a separate application. Based on the criteria below, determine the move groups for all the applications. Categorize the move groups in a sequential way like MG1, MG2, etc. Execute each criterion for all rows. If any criterion is not satisfied, proceed to the next criterion; otherwise, skip the next criterion.

Criteria 1:
If an application does not contain both 'Inbound Apps' and 'Outbound Apps', then consider it as a standalone application. Group all standalone applications as part of the same 'Move Group' and mention all the 'Application Name' under the 'Application Grouping' column.

Criteria 2:
If an application's 'Inbound Apps' or 'Outbound Apps' match those of another 'Application Name' in the spreadsheet, group all matching applications as part of the same 'Move Group' and mention all the matching 'Application Name' under the 'Application Grouping' column.

Sample input :
Application Name, Inbound Apps, Outbound Apps
Application1,,
Application2,Application3,
Application3,Application4,Application2
Application4,,Application4
Application5,,
Application6,Application7,
Application7,,Application6

Samplea output:
Move Group    Application Grouping                  Rationale
MG1           Application1,Application5             Standalone apps
MG2           Application2,Application3,Application4 Interdependent apps: Application2 is connected to Application3, Application3 is connected to Application4, and Application4 is connected to Application2
MG3           Application6,Application7             Interdependent apps: Application6 is connected to Application7, and Application7 is connected to Application6

If application name is present in Inbound apps or Outbound apps then those applications form a single movegroup.

Context is contained in <context> tags below.
<context>
{context}
</context>
{question}
Assistant:"""
movegroup_question = "Provide movegroup for all the applications in the provided context."
movegroup_input_file = "App-Inventory_v1.csv"
movegroup_output_spreadsheet = "App-movegroup-Analysis.xlsx"
movegroup_output_spreadsheet_agent = "App-movegroup-Analysis_agent.xlsx"