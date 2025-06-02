import requests     # импорт библиотеки Requests

url = 'https://api.chucknorris.io/jokes/random'     # url по которой будет отправляться запрос
print(url)

result = requests.get(url)     # отправка запроса
print(result.json())     # печать ответа запроса в формате json

assert result.status_code == 200
print('Статус-код корректен')

check_joke = result.json()     # охраняем в переменную тело нашего ответа в формате JSON
joke_value = check_joke.get("value")     # вызываем метод get(), в котором прописываем название поля
print(joke_value)