from llama_index.core import Document
from llama_index.core.node_parser import SimpleNodeParser
from llama_index.core.indices.keyword_table import SimpleKeywordTableIndex
import logging
import sys
import os
from dotenv import load_dotenv

load_dotenv()

# Настройка логирования
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))

# Создаем документы
documents = [
    Document(text="Abraham Lincoln was the 16th president of the United States."),
    Document(text="Abraham Shakespeare was a Florida lottery winner in 2006."),
    Document(text="William Shakespeare married Anne Hathaway."),
]

# Создаем простой индекс на основе ключевых слов вместо векторного
# SimpleKeywordTableIndex не требует модель эмбеддингов
node_parser = SimpleNodeParser()
nodes = node_parser.get_nodes_from_documents(documents)
index = SimpleKeywordTableIndex(nodes)

# Используем индекс для запросов
query_engine = index.as_query_engine()
response1 = query_engine.query("Who was Shakespeare's wife?")
print(response1)

response2 = query_engine.query("Did William Shakespeare win the lottery?")
print(response2)