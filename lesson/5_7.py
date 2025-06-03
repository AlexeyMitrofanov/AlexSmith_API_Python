import requests

#Продолжение предыдущего кейса 5_6
"""Отправка PUT-запроса"""
base_url = 'https://rahulshettyacademy.com'    # базовая url
key = '?key=qaclick123'                  # ключ допуска
put_resourse = '/maps/api/place/update/json'   # путь метода put

put_url = base_url + put_resourse + key
print(put_url)
new_address = "100 Lenina street, RU"
json_put_location = {                          # тело запроса put
            "place_id":place_id,               # переменная с place_id

            "address": new_address,             # переменная с новым адрессом

            "key":"qaclick123"
        }

result_put = requests.put(put_url, json=json_put_location)     # отпрвака запроса put, который включает url и тело запроса
print(result_put.json())

print(f'Статус-код: {result_put.status_code}')
assert result_put.status_code == 200, 'ОШИБКА, Статус-код не совпадают'
print('Статус-код PUT корректен')

check_response_put = result_put.json()

msg = check_response_put.get("msg")    # получение значения обязательного поля ответа
print(msg)
assert msg == 'Address successfully updated', 'ОШИБКА, Поле MSG некорректно'
print('Поле MSG корректно')


"""Отправка GET-запроса"""
result_get = requests.get(get_url)
print(result_get.json())

check_response_get = result_get.json()

print(f'Статус-код: {result_get.status_code}')
assert result_get.status_code == 200, 'ОШИБКА, Статус-код не совпадают'
print('Статус-код GET корректен')

actual_address = check_response_get.get('address')    # актуальный (фактический) адрес локации
print(actual_address)
assert actual_address == new_address, 'ОШИБКА, Адрес не изменился'
print('Адрес изменился')