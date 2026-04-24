import os
import sys
import argparse

from dotenv import load_dotenv
from google import genai
from google.genai import types
from prompts import system_prompt
from call_function import available_functions, call_function


def generate_content(client, messages):
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=messages,
        config=types.GenerateContentConfig(
            system_instruction=system_prompt, temperature=0, tools=[available_functions]
        ),
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

    for _ in range(20):
        response = generate_content(client, messages)

        # print(f"User prompt: {response.contents}")
        if response.usage_metadata is None:
            raise RuntimeError("No response usage metadata available. Request failed")

        if response.candidates:
            for candidate in response.candidates:
                messages.append(candidate.content)

        if args.verbose:
            print(f"User prompt: {args.user_prompt}")
            print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
            print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

        function_results = []

        if response.function_calls:
            for function in response.function_calls:
                function_call_result = call_function(function, verbose=args.verbose)

                if function_call_result.parts is None:
                    raise Exception

                if function_call_result.parts[0].function_response is None:
                    raise Exception

                function_results.append(function_call_result.parts[0])

                if args.verbose:
                    print(
                        f"-> {function_call_result.parts[0].function_response.response}"
                    )

            messages.append(types.Content(role="user", parts=function_results))

        else:
            print("Response:")
            print(response.text)
            return

    sys.exit(1)


if __name__ == "__main__":
    main()
