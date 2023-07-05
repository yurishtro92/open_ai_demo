import os
import openai

def init_api():
# Чтение переменных из файла .env, а именно API_KEY и ORG_ID
    with open(".env") as env:
        for line in env:
            key, value = line.strip().split("=")
            os.environ[key] = value
    # Инициализация ключа API и идентификатора организации
    openai.api_key = os.environ.get("API_KEY")
    openai.organization = os.environ.get("ORG_ID")
# Вызов API и получение списка моделей
init_api()

models = openai.Model.list()
for model in models["data"]:
    print(model["id"])
