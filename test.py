import json

data = {
    "name": "Alice",
    "age": 30,
    "hobbies": ["reading", "coding"]
}

# Запись в файл
with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

# Чтение из файла
with open("data.json", "r", encoding="utf-8") as f:
    loaded = json.load(f)

print(loaded["name"], loaded["age"])

