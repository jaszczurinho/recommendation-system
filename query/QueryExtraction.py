from google import genai
from google.genai import types

from query.StructuredOutput import *
from configuration.config import settings

client = genai.Client(api_key=settings.GEMINI_API_KEY)

with open('./master_prompt.txt', 'r') as f:
    master_prompt = f.read()

def get_model_response(query: str, prompt: str):
    response = client.models.generate_content(
       model="gemini-2.5-flash",
       config=types.GenerateContentConfig(
            system_instruction=prompt,
            response_mime_type="application/json",
            response_schema=UserRequest
       ),
        contents=query
    )
    return response

# print(query + '\n')
# print(get_model_response(query=query, prompt=master_prompt, ))
