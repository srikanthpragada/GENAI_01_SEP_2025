from openai import OpenAI
import keys 
import os

os.environ["OPENAI_API_KEY"] = keys.OPEN_AI_KEY

client = OpenAI()

response = client.responses.create(
    model="gpt-4o-mini",
    input="Write a one-sentence bedtime story about a unicorn."
)

print(response.output_text)