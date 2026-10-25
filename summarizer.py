import json
import sys
from pydantic import BaseModel
from google.genai import errors
from llm import ask


class Summary(BaseModel):
    title: str
    summary: str
    key_points: list[str]
    sentiment: str  # positive, neutral or negative


def summarize(path):
    # 1. Read the file safely
    try:
        with open(path, "r", encoding="utf-8") as f:
            text = f.read()
    except FileNotFoundError:
        print(f"File not found: {path}")
        return None

    if not text.strip():
        print("The file is empty.")
        return None

    # 2. Ask the model for JSON that matches the Summary shape
    response = ask(
        f"Summarize this text:\n\n{text}",
        system="You summarize text accurately. Use only the text provided.",
        temperature=0,
        json_schema=Summary,
    )

    # 3. response.parsed is a Summary object, or None if parsing failed
    if response.parsed is None:
        print("The model did not return valid JSON. Raw output:")
        print(response.text)
        return None
    return response.parsed


if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else "sample.txt"
    try:
        result = summarize(path)
    except errors.ClientError as e:  # 4xx: our request is wrong, no point retrying
        print(f"Request problem ({e.code}): {e.message}")
        result = None

    if result:
        with open("summary.json", "w", encoding="utf-8") as f:
            json.dump(result.model_dump(), f, indent=2)
        print("Saved summary.json")
        print(result.title)
        print(result.key_points)