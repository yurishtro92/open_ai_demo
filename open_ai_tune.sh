export OPENAI_API_KEY="<OPENAI_API_KEY>" #для инициализации работы с CLI API, авторизация терминала
openai tools fine_tunes.prepare_data -f data.json #для подготовки данных для тонкой настройки: data.json в data.jsonl
openai api fine_tunes.create -t "data_prepared.jsonl" -m curie #команда начать тонкую настройку
openai api fine_tunes.follow -i <YOUR_FINE_TUNE_JOB_ID> #продолжить настройку при прерывании со стороны API
openai api fine_tunes.list #список fine-tuned моделей
openai api fine_tunes.results -i <YOUR_FINE_TUNE_JOB_ID> #csv-файл анализа параметров fine-tuned модели

openai api fine_tunes.create -t "drug_malady_data_prepared_train.jsonl" -v "drug_malady_data_prepared_valid.jsonl" --compute_classification_metrics --classification_n_classes 3 -m ada --suffix "drug_malady_data"