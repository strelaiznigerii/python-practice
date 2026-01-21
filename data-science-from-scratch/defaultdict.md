# defaultdict

- один из видов словарей, который может автоматически присваивать значение по умолчанию новым ключам;
- у обычного словаря в таком случае вызывается ошибка `KeyError`

## import
```python
from collections import defaultdict
```

- пример ниже показывает, что далее каждый новый ключ получает пустой список
- необязательно можно передавать список, можно также передавать какие-то другие значения


```python
from collections import defaultdict

d = defaultdict(list)  # каждый новый ключ получает пустой список

d['Anna'].append('Python')
d['Anna'].append('Data Science')
d['Bob'].append('Java')

print(d)
# defaultdict(<class 'list'>, {'Anna': ['Python', 'Data Science'], 'Bob': ['Java']})
```


