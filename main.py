import os
import argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types

def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    if api_key is None:
        raise RuntimeError("API key wasn't found")

    client = genai.Client(api_key=api_key)

    parser = argparse.ArgumentParser(description="AI Agent")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()

    messages: list[types.Content] = [
        types.Content(role="user", parts=[types.Part(text=args.user_prompt)])
    ]
    response = client.models.generate_content(
        model="gemini-2.5-flash", contents=messages
    )
    if response.usage_metadata is None:
        raise RuntimeError("Usage metadata wasn't found")

    if args.verbose:
        print(f"""
User prompt: {args.user_prompt}
Prompt tokens: {response.usage_metadata.prompt_token_count}
Response tokens: {response.usage_metadata.candidates_token_count}
Response:
{response.text}
        """)
    else:
        print(response.text)

if __name__ == "__main__":
    main()
