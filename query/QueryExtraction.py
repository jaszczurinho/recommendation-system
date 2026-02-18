from google import genai
from google.genai import types

from query.StructuredOutput import *
from configuration.config import settings

client = genai.Client(api_key=settings.GEMINI_API_KEY)

with open('./master_prompt.txt', 'r') as f:
    master_prompt = f.read()

query = ""

response = client.models.generate_content(
   model="gemini-2.5-flash",
   config=types.GenerateContentConfig(
        system_instruction=master_prompt,
        response_mime_type="application/json",
        response_schema=UserRequest
   ),
    contents=query
)

print(query)
print(response.text)
