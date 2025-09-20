# Access gemini using langchain intergration with gemini api and use it to answer my query 


from langchain.chat_models import ChatGoogleGemini
from langchain.prompts import ChatPromptTemplate, HumanMessagePromptTemplate, SystemMessagePromptTemplate   


def query_gemini(prompt):
    chat = ChatGoogleGemini(model="gemini-1.5-pro", temperature=0)
    
    system_template = "You are a helpful assistant that helps to answer the user's query."
    system_message_prompt = SystemMessagePromptTemplate.from_template(system_template)
    
    human_message_prompt = HumanMessagePromptTemplate.from_template("{prompt}")
    
    chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])
    
    final_prompt = chat_prompt.format_messages(prompt=prompt)
    
    response = chat(final_prompt)
    
    return response.content   



if __name__ == "__main__":
    query = "What courses are available?"
    response = query_gemini(query)
    print(response)
