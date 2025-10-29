import argparse
import os
import sys

from dotenv import load_dotenv
from google import genai
from google.genai import types


load_dotenv()
API_KEY = os.environ.get("GEMINI_API_KEY")


def parse_args():
    parser = argparse.ArgumentParser(
        prog="bootloader_ai_agent",
        description="Take a prompt arg from the command line and send to Gemini LLM",
    )
    parser.add_argument("user_prompt")
    parser.add_argument("--verbose", action="store_true")
    return parser.parse_args()


def main():
    args = parse_args()
    client = genai.Client(api_key=API_KEY)
    model = "gemini-2.0-flash-001"

    messages = [
        types.Content(role="user", parts=[types.Part(text=args.user_prompt)])
    ]
    response = client.models.generate_content(model=model, contents=messages)

    print(response.text)

    if args.verbose:
        print(f"User prompt: {args.user_prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")


if __name__ == "__main__":
    main()
