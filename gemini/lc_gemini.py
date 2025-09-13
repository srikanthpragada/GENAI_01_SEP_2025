#pip install langchain-google-genai google-generativeai
#Create key using https://aistudio.google.com/apikey

import keys 

from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash",google_api_key= keys.GOOGLEKEY)

# Use invoke with a list of messages
response = llm.invoke("What's the capital of Spain?")
print(response.content)
 
