######################################### Server Mapping Input Details ################################################
server_mapping_prompt = """
\n\nHuman: From the given source of context, analyse the data in each column. The provided context contains details regarding the servers that are used across multiple applications for Discovery and Assessment purpose. Your job is to provide the ApplicationName to ServerName mapping.If one Application is using multiple Servers, please consolidate the details for all servers separated by comma.
The response should be in a html tabular format with the column names as following: ApplicationName, ServerName, ServerCategory, ServerType. The criteria to evaluate ServerCategory and ServerType is explained below.

ServerCategory should be evaluated as per the below criteria:
1. If the fourth character of the ServerName is 'P', then the ServerCategory should be Production.
2. If the fourth character of the ServerName is 'T', then the ServerCategory should be Test.
2. If the fourth character of the ServerName is 'D', then the ServerCategory should be Dev.

ServerType should be evaluated as per the below criteria:
1. If the ServerName contains 'DB' in the exact letter sequence only, then the ServerType will be 'Database Server'.
2. If the ServerName doesn't contain the letter sequence 'DB', then the ServerType will be 'Application Server'.

**Provide the result in HTML table format**.

Context is contained in <context> tags below.

<context>
{context}
</context>

{question}

Assistant:"""

server_mapping_question = "Provide the details of all the servers based on the ApplicationName."
server_mapping_input_file = "Server-Inventory_v1.csv"
server_mapping_db_name = "faiss_db_server_mapping"
server_mapping_output_spreadsheet = "App-Server-Mapping.xlsx"
server_mapping_output_spreadsheet_agent = "App-Server-Mapping_agent.xlsx"