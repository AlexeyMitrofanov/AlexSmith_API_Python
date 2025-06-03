import requests

class TestCreateNewLocation:

    def __init__(self):
        pass

    """Создание новой локации 5 раз и запись place_id в файл"""
    def test_create_new_location(self):
        base_url = 'https://rahulshettyacademy.com'  # базовая URL
        key = '?key=qaclick123'                       # ключ доступа
        post_resource = '/maps/api/place/add/json'    # путь для POST-запроса

        post_url = base_url + post_resource + key
        print(post_url)

        # Открываем файл для записи place_id
        file = open('place_id.txt', 'w')  # открываем файл в режиме записи

        for i in range(5):  # цикл для отправки 5 запросов
            # Тело запроса
            json_new_location = {
                "location": {
                    "lat": -38.383494 + i,  # изменяем координаты
                    "lng": 33.427362 + i
                },
                "accuracy": 50,
                "name": f"Frontline house {i + 1}",  # уникальное имя для каждого запроса
                "phone_number": "(+91) 983 893 3937",
                "address": "29, side layout, cohen 09",
                "types": ["shoe park", "shop"],
                "website": "http://google.com",
                "language": "French-IN"
            }

            # Отправка POST-запроса
            result_post = requests.post(post_url, json=json_new_location)
            print(result_post.json())  # выводим ответ сервера

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
            file.write(place_id + '\n')  # записываем place_id в файл
            print(f'Поле place_id: {place_id}')
        file.close()

        """Проверка созданных локаций"""
    def test_check_location(self):
        base_url = 'https://rahulshettyacademy.com'    # базовая url
        key = '?key=qaclick123'                  # ключ допуска
        get_resourse = '/maps/api/place/get/json'     # путь метода get

        file = open('place_id.txt', 'r')
        place_ids = file.readlines()
        for place_id in place_ids:
            place_id = place_id.strip()  # Удаляем лишние пробелы и \n
            get_url = base_url + get_resourse + key + "&place_id=" + place_id     # добавление в url идентификатора place_id из файла
            print(get_url)
            # Отправка GET-запроса
            result_get = requests.get(get_url)
            print(result_get.json())

            print(f'Статус-код: {result_get.status_code}')
            assert result_get.status_code == 200, 'ОШИБКА, Статус-код не совпадают'
            print('Статус-код GET-запроса корректен')
        file.close()

test = TestCreateNewLocation()
test.test_create_new_location()
test.test_check_location()