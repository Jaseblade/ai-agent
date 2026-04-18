import os
import argparse

from dotenv import load_dotenv
from google import genai
from google.genai import types


def generate_content(client, messages):
    response = client.models.generate_content(
        model='gemini-2.5-flash', 
        contents=messages
    )
    return response

def main():
    parser = argparse.ArgumentParser(description="AI Agent")

    parser.add_argument("user_prompt", type=str, help="User prompt to send to Gemini")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")

    args = parser.parse_args()


    load_dotenv()
    try:
        api_key = os.environ.get("GEMINI_API_KEY")
    except:
        raise RuntimeError("The GEMINI_API_KEY environment variable was not found")


    client = genai.Client(api_key=api_key)
    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]
    response = generate_content(client, messages)

    # print(f"User prompt: {response.contents}")
    if response.usage_metadata is None:
        raise RuntimeError("No response usage metadata available. Request failed")
    
    if args.verbose:
        print(f"User prompt: {args.user_prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
        
    print("Response:")
    print(response.text)

if __name__ == "__main__":
    main()
