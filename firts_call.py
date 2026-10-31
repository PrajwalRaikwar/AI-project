import os
from dotenv import load_dotenv
# pip install openai
from openai import OpenAI
load_dotenv()                 # loads everything from .env

client = OpenAI(api_key=os.getenv("GROQ_API_KEY"),base_url="https://api.groq.com/openai/v1"
    ) 

# reads your API key from the environment

response = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[
        {"role": "system", "content": "You are a rude run guide."},
        {"role": "user",   "content": "Suggest one thing to do in londan."},
    ],
)
print(response.choices[0].message.content)


# now OpenAI() finds the key automatically — no key in your code 🎉