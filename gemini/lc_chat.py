import keys 
import os 
from langchain.chat_models import init_chat_model

os.environ["GOOGLE_API_KEY"] = keys.GOOGLEKEY

model = init_chat_model("gemini-2.5-flash", model_provider="google_genai")

response = model.invoke("What is the capital of France?")
print(response.content)
print(response.usage_metadata['output_tokens'])

