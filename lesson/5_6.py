import requests

"""Отправка POST-запроса"""
base_url = 'https://rahulshettyacademy.com'    # базовая url
key = '?key=qaclick123'                  # ключ допуска
post_resourse = '/maps/api/place/add/json'     # путь метода post

post_url = base_url + post_resourse + key
print(post_url)
json_new_location = {                          # тело запроса post
            "location": {
                "lat": -38.383494,
                "lng": 33.427362
            }, "accuracy": 50,
            "name": "Frontline house",
            "phone_number": "(+91) 983 893 3937",
            "address": "29, side layout, cohen 09",
            "types": [
                "shoe park",
                "shop"
            ],
            "website": "http://google.com",
            "language": "French-IN"
        }

result_post = requests.post(post_url, json=json_new_location)     # отпрвака запроса post, который включает url и тело запроса
print(result_post.json())

print(f'Статус-код: {result_post.status_code}')
assert result_post.status_code == 200, 'ОШИБКА, Статус-код не совпадают'
print('Статус-код POST корректен')

check_response_post = result_post.json()

status = check_response_post.get("status")    # получение значения обязательного поля ответа
print(status)
assert status == 'OK', 'ОШИБКА, Поле Status некорректно'
print('Поле Status корректно')

assert 'place_id' in check_response_post
print("Поле place_id присутствует в теле ответа")
place_id = check_response_post.get("place_id")
print(f'Поле place_id: {place_id}')


"""Отправка GET-запроса"""
base_url = 'https://rahulshettyacademy.com'    # базовая url
key = '?key=qaclick123'                  # ключ допуска
get_resourse = '/maps/api/place/get/json'     # путь метода get


get_url = base_url + get_resourse + key + "&place_id=" + place_id     # добавление в url идентификатора place_id
print(get_url)

result_get = requests.get(get_url)
print(result_get.json())

print(f'Статус-код: {result_get.status_code}')
assert result_get.status_code == 200, 'ОШИБКА, Статус-код не совпадают'
print('Статус-код GET корректен')
