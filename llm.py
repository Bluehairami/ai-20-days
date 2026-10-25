import time
from dotenv import load_dotenv
from google import genai
from google.genai import types, errors

load_dotenv(override=True)

MODEL = "gemini-3.8-flash"  # update from AI Studio if it changes
client = genai.Client(http_options=types.HttpOptions(timeout=60000))  # 60s, in milliseconds


def ask(prompt, system="You are a helpful assistant.", temperature=0.3,
        json_schema=None, max_attempts=4):
    extra = {}
    if json_schema:
        extra = {"response_mime_type": "application/json",
                 "response_schema": json_schema}

    config = types.GenerateContentConfig(
        system_instruction=system,
        temperature=temperature,
        max_output_tokens=3000,
        **extra,
    )

    wait = 2
    for attempt in range(1, max_attempts + 1):
        try:
            return client.models.generate_content(
                model=MODEL, contents=prompt, config=config
            )
        except errors.ServerError as e:  # 5xx: server's fault, worth retrying
            print(f"Server busy (attempt {attempt}/{max_attempts}): {e.code}. Waiting {wait}s...")
            time.sleep(wait)
            wait *= 2

    raise RuntimeError("Gemini is still unavailable. Try again later.")

    #  COMMON CODE TO BE EXECUTED FOR 