#curie:ft-personal-2023-07-11-15-38-39 fine tuned model id

import os
import openai
def init_api():
    with open(".env") as env:
        for line in env:
            key, value = line.strip().split("=")
            os.environ[key] = value
    openai.api_key = os.environ.get("API_KEY")
    openai.organization = os.environ.get("ORG_ID")

init_api()

model = "curie:ft-personal-2023-07-11-15-38-39"

drugs = [
"A CN Gel(Topical) 20gmA CN Soap 75gm", # Класс 0
"Addnok Tablet 20'S", # Класс 1
"ABICET M Tablet 10's", # Класс 2
]

for drug_name in drugs:
    prompt = "Drug: {}\nMalady:".format(drug_name)
    response = openai.Completion.create(
        model=model,
        prompt= prompt,
        temperature=1,
        max_tokens=1,
        )
    # Выводим на п сгенерированный текст
    drug_class = response.choices[0].text
    # Вывод должен содержать 0, 1 и 2
    print(drug_class)