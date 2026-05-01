import os

from crewai import Agent, LLM
from dotenv import load_dotenv

load_dotenv()

# For switching between OpenAI and OpenRouter, we can check for the presence of API keys in environment variables. This allows us to easily switch between providers without changing the code. 

# openai_api_key = os.getenv("OPENAI_API_KEY") 
# openrouter_api_key = os.getenv("OPENROUTER_API_KEY")

# if openai_api_key:
#     llm = LLM(
#         model="gpt-4o",
#         api_key=openai_api_key,
#         # temperature=0.2,  # Optional: Adjust the creativity of the responses
#     )

# elif openrouter_api_key:
#     llm = LLM(
#         model="openai/gpt-4o",
#         api_key=openrouter_api_key,
#         base_url="https://openrouter.ai/api/v1",
#     )

# else:
#     raise ValueError("Set OPENAI_API_KEY or OPENROUTER_API_KEY in .env")

groq_api_key = os.getenv("GROQ_API_KEY")

llm = LLM(
    model="llama-3.1-8b-instant",
    api_key=groq_api_key,
    base_url="https://api.groq.com/openai/v1",
    temperature=0.2,
)

# Define your agent with OpenAI LLM
hate_speech_detector = Agent(
    role="Hate Speech Detector",
    goal="Analyse the text and identify if any hate speech / offensive language is present",
    llm=llm,
    backstory=(
        "You are a Hate Speech Detector for Twitter who understands details very well and experienced in detecting harmful content. "
        "You can identify hate speech / offensive language in given tweet."
    ),
)