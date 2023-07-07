#ft-4AYPH5qAthpL0Pe6YuCr8HuC curie (example)
#ft-C9LhZeUvaaAk5qo6HqylQFKB curie (example)

#ft-3I5rYtHb9QR0hhCeEJczUCSv ada (medicine bot)
import pandas as pd
# Читаем первые n строк
n = 2000
df = pd.read_excel('Medicine_description.xlsx', sheet_name='Sheet1', header=0,
nrows=n)
# Получаем уникальные значения из столбца Reason (причина)
reasons = df["Reason"].unique()
# Присваиваем номер каждой причине
reasons_dict = {reason: i for i, reason in enumerate(reasons)}
# Добавляем символ новой строки и ### в конец каждого описания
df["Drug_Name"] = "Drug: " + df["Drug_Name"] + "\n" + "Malady:"
# Объединяем столбцы Reason и Description
df["Reason"] = " " + df["Reason"].apply(lambda x: "" + str(reasons_dict[x]))
# Удаляем столбец Reason
df.drop(["Description"], axis=1, inplace=True)
# Переименовываем столбцы
df.rename(columns={"Drug_Name": "prompt", "Reason": "completion"},
inplace=True)
# Конвертируем кадр данных в формат jsonl
jsonl = df.to_json(orient="records", indent=0, lines=True)
# Записываем jsonl в файл
with open("drug_malady_data.jsonl", "w") as f:
    f.write(jsonl)