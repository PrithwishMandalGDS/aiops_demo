aiops_microsoft_advisor_agent_system_message = """
    Azure Advisor has raised a impact_level impact recommendation, 
    Under category category. Impacted field is provider_name in Azure. 
    Identified problem is problem_statement. 
    Please convert the whole dataset of json into a dataframe using python code. If you want to use spark or anything use that and create a dataframe
    """
aiops_microsoft_advisor_question = "Give a detailed solution for every problem statements present in the json dataset and the steps to implement it."


aiops_advisor_agent_system_message_dtf = """
    Azure advisor has created a dataset in csv file which contains columns like 'id', 'name', 'type', 'category', 'impact', 'impacted_field',    
       'impacted_value', 'last_updated', 'recommendation_type_id',      
       'short_description', 'resource_metadata', 'extended_properties'.
    'Problem' is actually a problem statement and column impact consists of mainly HIGH, LOW, MEDIUM.
    """
 # When the values for resource_id field are same consider a record as duplicate and remove duplicates.

aiops_advisor_question_dtf = "Select 'id' and 'Problem' column of the rows which have impact value HIGH"

aiops_advisor_agent_system_message_sol = """
The csv file contains two columns. 1st column is id and 2nd column is problem statement.
Take every problem statement at a time and give the detailed solution.
"""
aiops_advisor_question_sol = """list down all the problem statements in the 2nd column. If the problem statements are duplicate also , I want to get all the statements. I also solution with respect to every problem statements you are listing down. Problem and solution should be like this : number. "problem statement" - """