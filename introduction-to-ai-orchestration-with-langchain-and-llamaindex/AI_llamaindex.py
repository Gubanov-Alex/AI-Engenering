# pip install llama-index-llms-openai-like
import os
from dotenv import load_dotenv

load_dotenv()

from llama_index.core.llms import ChatMessage
# Используем основной импорт для OpenAI из llama_index
from llama_index.llms.openai import OpenAI


application_prompt = """Given the following short description
    of a particular topic, write 3 attention-grabbing headlines 
    for a blog post. Reply with only the titles, one on each line,
    with no additional text.
    DESCRIPTION:
"""
user_input = """AI Orchestration with LangChain and LlamaIndex
    keywords: Generative AI, applications, LLM, chatbot"""

llm = OpenAI(
    api_key=os.environ.get('OPENAI_API_KEY'),
    is_chat_model=True,
    #api_base="http://localhost:12/v1",
    temperature=0.7,
    max_tokens=500,
    model="gpt-4-1106-preview"
)
messages = [
    ChatMessage(role="system", content=application_prompt),
    ChatMessage(role="user", content=user_input),
]
results = llm.chat(messages)

print(results)

# for streaming use
#resp = llm.stream_chat(messages)
#for chunk in resp:
#    print(chunk.delta, end="")