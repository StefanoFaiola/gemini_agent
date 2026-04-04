import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import argparse
from agent.prompts import system_prompt
from agent.call_function import available_functions, call_function
import sys
from config import MAX_ITERS


def main():
    parser = argparse.ArgumentParser(description='Chatbot')
    parser.add_argument('user_prompt', type=str, help= "User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()

    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    if api_key is None:
        raise RuntimeError("Environment variable not found")


    client = genai.Client(api_key=api_key)
    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]

    for _ in range(21):
        try:
            last_response = generate_content(client, messages, args.user_prompt, args.verbose)
            if last_response:
                print("Final response:")
                print(last_response)
                return
        except Exception as e:
            print(f"Error in generate_content: {e}")



    print(f"Maximum iterations ({MAX_ITERS}) reached")
    sys.exit(1)
        

    

def generate_content(client, messages, prompt, verbose):
    response = client.models.generate_content(
        model= "gemini-2.5-flash",
        contents= messages,
        config = types.GenerateContentConfig(
            system_instruction=system_prompt,
            tools=[available_functions]),
        )
    
    if response.candidates:
        for c in response.candidates:
            if c.content:
                messages.append(c.content)


    prompt_tokens = response.usage_metadata.prompt_token_count
    response_tokens = response.usage_metadata.candidates_token_count

    if not response.usage_metadata:
        raise RuntimeError("Gemini API response appears to be malformed")

    if verbose:
        print(f"User prompt: {prompt}")
        print(f"Prompt tokens: {prompt_tokens}")
        print(f"Response tokens: {response_tokens}")

    if not response.function_calls:
        return response.text
    
    function_results = []

    for function_call in response.function_calls:
        print(f"Calling function: {function_call.name}({function_call.args})")
        function_call_result = call_function(function_call, verbose)

        if function_call_result.parts == "" or function_call_result.parts is None:
            raise Exception(".parts is empty")
        if function_call_result.parts[0].function_response is None:
            raise Exception("function_response is None")
        if function_call_result.parts[0].function_response.response is None:
            raise Exception("No function results")
        
        function_results.append(function_call_result.parts[0])

        if verbose:
            print(f"-> {function_call_result.parts[0].function_response.response}")

    messages.append(types.Content(role="user", parts=function_results))

if __name__ == "__main__":
    main()
