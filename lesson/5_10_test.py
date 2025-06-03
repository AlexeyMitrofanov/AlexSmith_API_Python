import requests

class TestLocation:

    def __init__(self):
        self.base_url = 'https://rahulshettyacademy.com'  # базовая URL
        self.key = '?key=qaclick123'                       # ключ доступа
        self.post_resource = '/maps/api/place/add/json'    # путь для POST-запроса
        self.delete_resource = '/maps/api/place/delete/json'  # путь для DELETE-запроса
        self.get_resource = '/maps/api/place/get/json'     # путь для GET-запроса

    """Создание новой локации 5 раз и запись place_id в файл"""
    def test_create_new_location(self):
        post_url = self.base_url + self.post_resource + self.key
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
            assert status == 'OK', 'ОШИБКА, Поле Status некорректно'
            print('Поле Status корректно')

            assert 'place_id' in check_response_post
            place_id = check_response_post.get("place_id")
            file.write(place_id + '\n')  # записываем place_id в файл
            print(f'Поле place_id: {place_id}')
        file.close()

    """Удаление 2-го и 4-го place_id из файла"""
    def test_delete_locations(self):
        delete_url = self.base_url + self.delete_resource + self.key
        print(delete_url)

        # Чтение place_id из файла
        file = open('place_id.txt', 'r')  # открываем файл в режиме чтения
        place_ids = file.readlines()

        # Удаляем 2-й и 4-й place_id
        for k in [1, 3]:  # индексы для удаления (0-основанные)
            place_id = place_ids[k].strip()
            json_delete_location = {"place_id": place_id}

            # Отправка DELETE-запроса
            result_delete = requests.delete(delete_url, json=json_delete_location)
            print(result_delete.json())

            print(f'Статус-код удаления: {result_delete.status_code}')
            assert result_delete.status_code == 200, 'ОШИБКА, Статус-код удаления некорректен'
            print('Статус-код DELETE корректен')
        file.close()

    """Проверка существующих локаций и запись их в новый файл"""
    def test_check_location(self):
        get_url = self.base_url + self.get_resource + self.key
        existing_places = []

        # Чтение place_id из файла
        file = open('place_id.txt', 'r')  # открываем файл в режиме чтения
        place_ids = file.readlines()

        for place_id in place_ids:
            place_id = place_id.strip()  # Удаляем лишние пробелы и \n
            response = requests.get(get_url + "&place_id=" + place_id)  # добавление в url идентификатора place_id
            print(response.json())

            if response.status_code == 200:
                existing_places.append(place_id)  # добавляем существующий place_id в список
                print(f'Существующий place_id: {place_id} добавлен в список')
            else:
                    print(f'place_id: {place_id} не существует')

        # Запись существующих локаций в новый файл
        new_file = open('existing_place_id.txt', 'w')  # открываем файл в режиме записи
        for place in existing_places[:3]:  # берем только первые 3 существующие локации
            new_file.write(place + '\n')
            print(f'Существующий place_id записан в файл: {place}') # выводим на печать успех

# Запуск тестов
test = TestLocation()
test.test_create_new_location()
test.test_delete_locations()
test.test_check_location()
