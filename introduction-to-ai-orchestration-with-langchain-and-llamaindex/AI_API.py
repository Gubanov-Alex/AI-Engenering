import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
# AI_API.py

# Константы для настроек модели
MODEL_NAME = "gpt-4-1106-preview"
# MODEL_NAME = "qwen/qwen3-8b"
# MODEL_NAME = "microsoft/phi-4-mini-reasoning"
MAX_TOKENS = 200
TEMPERATURE = 0.7

# Константы для промптов
SYSTEM_PROMPT = """Given the following short description
of a particular topic, write 3 attention-grabbing headlines 
for a blog post. Reply with only the titles, one on each line,
with no additional text.
DESCRIPTION:
"""


def generate_headlines(topic_description, model_name=MODEL_NAME, 
                      max_tokens=MAX_TOKENS, temperature=TEMPERATURE):
    """
    Генерирует три привлекательных заголовка для блога на основе описания темы.
    
    Args:
        topic_description (str): Описание темы и ключевые слова
        model_name (str): Название модели OpenAI для использования
        max_tokens (int): Максимальное количество токенов в ответе
        temperature (float): Параметр креативности (0.0-1.0)
        
    Returns:
        str: Три заголовка, каждый на новой строке
    """
    client = OpenAI(
         api_key=os.environ['OPENAI_API_KEY'],  # это стандартное поведение
         # base_url="http://127.0.0.1:1234/v1"    # см. раздел 1 видео 3
    )
    
    response = client.chat.completions.create(
        model=model_name,
        max_tokens=max_tokens,
        temperature=temperature,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": topic_description}
        ]
    )
    
    return response.choices[0].message.content


def main():
    topic = """AI Orchestration with LangChain and LlamaIndex
keywords: Generative AI, applications, LLM, chatbot"""
    
    headlines = generate_headlines(topic)
    print(headlines)


if __name__ == "__main__":
    main()