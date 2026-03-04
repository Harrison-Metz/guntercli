import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
if api_key == None:
    raise RuntimeError("api key not found")
client = genai.Client(api_key=api_key)
response = client.models.generate_content(model="gemini-2.5-flash", contents="Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum.")
metadata = response.usage_metadata
if metadata != None:
    print(f"Prompt tokens: {metadata.prompt_token_count}")
    print(f"Response tokens: {metadata.candidates_token_count}")
else:
    raise RuntimeError("failed api request")

print(f"Response: {response.text}")

def main():
    print("Hello from guntercli!")


if __name__ == "__main__":
    main()
