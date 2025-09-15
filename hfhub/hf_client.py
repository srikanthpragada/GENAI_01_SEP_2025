# Access LLM without any context 

from huggingface_hub import InferenceClient

import keys 
model_id = "mistralai/Mistral-7B-Instruct-v0.3"
client = InferenceClient(model=model_id, 
                         token=keys.HUGGINGFACE_KEY)

while True:
    prompt = input("Query [q to quit] :")
    if prompt.lower() == 'q':
        break
            
    
    ai_response = client.chat_completion([{"role": "user", "content": prompt}])
    response = ai_response.choices[0].message.content
    print(response)
    print("-" * 80)

    

