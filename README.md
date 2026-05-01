# Twitter Hate Speech Detector

A small CrewAI-powered project for detecting hate speech in text using a Groq-compatible LLM.

## Project Structure

- `agents.py` — defines the `Hate Speech Detector` agent and configures the LLM.
- `tasks.py` — defines the hate speech detection task prompt and expected output.
- `crew.py` — boots the Crew, runs the detection task, and prints the result.
- `.env` — stores secret API keys like `GROQ_API_KEY`.
- `.gitignore` — ignores the local Python environment, cache files, and `.env`.

## Requirements

- Python 3.8+
- `crewai`
- `python-dotenv`

## Setup

1. Create and activate a virtual environment (recommended):
   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

2. Install dependencies:
   ```powershell
   pip install crewai python-dotenv
   ```

3. Create or update `.env` with your Groq API key:
   ```text
   GROQ_API_KEY=gsk_...
   ```

## Run

From the project root:

```powershell
python crew.py
```

If you use `uv` and have it installed, you can also run:

```powershell
uv run crew.py
```

## Customize Input

Edit the `Text` variable in `crew.py` to analyze different sentences.

## Notes

- The agent currently uses the Groq endpoint and a compatible model in `agents.py`.
- Do not commit `.env` to source control; the `.gitignore` file already excludes it.


