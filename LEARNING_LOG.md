# Learning Log

## Day 1: First LLM API call

### Words I learned
- **Token:** a small piece of text. I pay for the tokens I send and receive.
- **Context window:** how much text the model can look at once, like the size of a desk.
- **Temperature:** the creativity dial. Low gives careful, repeatable answers; high gives more varied ones.
- **System prompt:** the model's job description, given before the user's question.
- **Model:** a trained "brain" that predicts the next piece of text. I use it through an API.

### What I built
- Set up Python, VS Code, Git, a virtual environment and a GitHub repo.
- Got a free Gemini API key from Google AI Studio and stored it in `.env`, with `.env` in `.gitignore`.
- Wrote `hello_llm.py`, which sends a question to Gemini and prints the answer and token usage.

### Problems I fixed
- **File not found:** I had two `ai-20-days` folders and the script was in the wrong one. Lesson: run commands from the folder that holds the files, and check with `dir`.
- **"API key not valid":** I had edited the key. Google's new keys start with `AQ.`, and a key only works exactly as it is copied. I made a new key and pasted it unchanged.
- **404 model not found:** the old model name was retired. I switched to the name Google recommended in the error message.
- **Answer cut off:** the usage data showed most of my token limit went to the model's hidden thinking tokens, so I raised `max_output_tokens`.
- **503 server busy:** this is Google's server being overloaded, not my mistake. 4xx errors mean my request is wrong; 5xx errors mean the server has a problem.

### Experiments (fill in after running them)
- Temperature 0 vs 1: ______
- System prompt changed to a pirate: ______
- Small `max_output_tokens`: ______
- Longer question, token count: ______

## Day 2: Reusable helper and JSON summarizer

### Words I learned
- **JSON:** structured data written as text, with named fields that code can read.
- **Schema:** the exact shape I want back (title, summary, key points, sentiment).
- **Parse / validate:** turn text into data and check that it matches the shape.
- **Exponential backoff:** wait longer after each failed try (2s, 4s, 8s).

### What I built
- `llm.py`: a helper that talks to Gemini, with a timeout and retries on server errors.
- `summarizer.py`: reads `sample.txt`, asks for JSON that matches a `Summary` form, and saves `summary.json`.
- `sample.txt` (document to read) and `empty.txt` (blank file for a test).

### What I learned
- Only 5xx errors are worth retrying. A wrong key or model should fail immediately.
- Putting the Gemini code in one file means every later project can reuse it.
- Asking for a fixed JSON shape turns a paragraph into data a program can use.

### Failure tests (fill in after running them)
- Missing file: ______
- Empty file: ______
- Wrong API key: ______
- Same file 3 times at temperature 0: ______

### Still unclear / questions
- ______