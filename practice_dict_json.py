import json
import os

file_path = 'data.json'

if not os.path.exists(file_path):
    name = str(input('Введите имя: '))
    age = int(input('Введите возраст: '))
    data = { 
            "name" : name, 
            "age": age
           } 

    with open(file_path, "w", encoding="utf-8") as f:
         json.dump(data, f)
         print("Данные сохранены!")
else:
     with open(file_path, "r", encoding="utf-8") as f:
         loaded = json.load(f)
    
     print(f'Привет, {loaded["name"]}! Вам {loaded["age"]} лет.')

 
