import json
import pytest
from utils.api import GoogleMapsApi
from utils.checking import Checking   # импорт содержимого модуля checking



class TestCreatePlace():
    """Класс содержащий тест по работе с локацией"""

    def test_create_new_place(self):
        """Тест по созданию, изменение и удаление новой локации"""

        print("Метод POST")
        result_post = GoogleMapsApi.create_new_place()  # вызов метода по созданию новой локации
        Checking.check_status_code(result_post, 200)  # вызов метода по проверке статус-кода

        check_post = result_post.json()
        place_id = check_post.get("place_id")  # получения place_id для метода GET

        print("Метод GET для проверки POST")
        result_get = GoogleMapsApi.get_new_place(place_id)  # отправка метода Get
        Checking.check_status_code(result_get, 200)  # вызов метода по проверке статус-кода
        print(result_get.json())

        print("Метод PUT")
        result_put = GoogleMapsApi.put_new_place(place_id)
        Checking.check_status_code(result_put, 200)  # вызов метода по проверке статус-кода
        print(result_get.json())

        print("Метод GET для проверки PUT")
        result_get = GoogleMapsApi.get_new_place(place_id)  # отправка метода Get
        Checking.check_status_code(result_get, 200)  # вызов метода по проверке статус-кода
        print(result_get.json())

        print("Метод DELETE")
        result_delete = GoogleMapsApi.delete_new_place(place_id)  # удаление данных о созданной локации
        Checking.check_status_code(result_delete, 200)  # вызов метода по проверке статус-кода
        print(result_get.json())

        print("Метод GET для проверки DELETE")
        result_get = GoogleMapsApi.get_new_place(place_id)  # отправка метода Get
        Checking.check_status_code(result_get, 404)  # вызов метода по проверке статус-кода
        print(result_get.json())