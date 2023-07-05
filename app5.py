import os
import openai
import pandas as pd
from openai.embeddings_utils import get_embedding
from openai.embeddings_utils import cosine_similarity
from sklearn.metrics import precision_score



def init_api():
    with open(".env") as env:
        for line in env:
            key, value = line.strip().split("=")
            os.environ[key] = value
    openai.api_key = os.environ.get("API_KEY")
    openai.organization = os.environ.get("ORG_ID")


init_api()
categories = [
"POLITICS",
"WELLNESS",
"ENTERTAINMENT",
"TRAVEL",
"STYLE & BEAUTY",
"PARENTING",
"HEALTHY LIVING",
"QUEER VOICES",
"FOOD & DRINK",
"BUSINESS",
"COMEDY",
"SPORTS",
"BLACK VOICES",
"HOME & LIVING",
"PARENTS",
]
def classify_sentence(sentence):
    # Получение встраивания предложения
    sentence_embedding = get_embedding(sentence, engine="text-embedding-ada-002")
    # Вычисление сходства между предложением и каждой категорией
    similarity_scores = {}
    for category in categories:
        category_embeddings = get_embedding(category, engine="text-embedding-ada-002")
        similarity_scores[category] = cosine_similarity(sentence_embedding, category_embeddings)
    # Возвращаем категорию с наивысшей оценкой сходства
    return max(similarity_scores, key=similarity_scores.get)

def evaluate_precision(categories):
    # Загрузка набора данных
    df = pd.read_json("data/News_Category_Dataset_v3.json", lines=True).head(20)
    y_true = []
    y_pred = []
    # Классификация каждого предложения
    for _, row in df.iterrows():
        true_category = row['category']
        predicted_category = classify_sentence(row['headline'])
        y_true.append(true_category)
        y_pred.append(predicted_category)

    # if true_category != predicted_category:
    #     print("Ложный прогноз: {:50} Истина: {:20} Прогноз: {:20}".format(row['headline'], true_category, predicted_category))
    # else:
    #     print("Истинный прогноз: {:50} Истина: {:20} Прогноз:{:20}".format(row['headline'], true_category, predicted_category))
    # Вычисление показателя точности
    return precision_score(y_true, y_pred, average='micro', labels=categories)


precision_evaluated = evaluate_precision(categories)
print("Точность: {:.2f}".format(precision_evaluated))