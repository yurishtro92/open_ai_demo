import os
import openai


def init_api():
    with open(".env") as env:
        for line in env:
            key, value = line.strip().split("=")
            os.environ[key] = value

init_api()
openai.api_key = os.environ.get("API_KEY")
openai.organization = os.environ.get("ORG_ID")
next = openai.Completion.create(
    model="text-davinci-003",
    prompt="Once upon a time",
    max_tokens=7,
    temperature=0
)
print(next)