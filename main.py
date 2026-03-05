import os
import argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types

parser = argparse.ArgumentParser(description="guntercli")
parser.add_argument("user_prompt", type=str, help="User prompt")
args = parser.parse_args()

messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
if api_key == None:
    raise RuntimeError("api key not found")
client = genai.Client(api_key=api_key)
response = client.models.generate_content(model="gemini-2.5-flash", contents=messages)
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
