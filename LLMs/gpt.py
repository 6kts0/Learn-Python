"""
Initialize a .env file to hide your API key
"""

from openai import OpenAI

API_KEY = 'your-key'

client = OpenAI()

 
usr_prompt = input("Prompt: ")
system_struct = "Do not exceed a 500 word cap in our responses"

response = client.responses.create(
    input = usr_prompt,
    instructions = system_struct,
    model = 'gpt-4.5'
)

print(response.output_text)