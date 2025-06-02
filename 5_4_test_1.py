import requests


class Test_joke():
    """Получение категорий и шуток"""

    def __init__(self):
        pass

    def test_get_joke_from_categories(self):
        """Получение списка категорий"""
        url_get_categories = "https://api.chucknorris.io/jokes/categories"
        print(url_get_categories)
        result_categories = requests.get(url_get_categories)
        print("Статус код : " + str(result_categories.status_code))
        assert 200 == result_categories.status_code
        if result_categories.status_code == 200:
            print("Запрос выполнен успешно! Получен список возможных категорий для шуток")
        else:
            print("Ошибка, запрос не выполнен!")
        result_categories.encoding = 'utf-8'
        categories = result_categories.json()
        print(categories)

        """Получение одной шутки из каждой категории"""
        for category in categories:
            print("\nВыбрана категория: " + category)
            url_get_joke_from_category = "https://api.chucknorris.io/jokes/random?category=" + category
            print(url_get_joke_from_category)
            result_joke = requests.get(url_get_joke_from_category)
            print("Статус код : " + str(result_joke.status_code))
            assert 200 == result_joke.status_code
            if result_joke.status_code == 200:
                print("Запрос выполнен успешно! Получена шутка из категории: " + category)
            else:
                print("Ошибка, запрос не выполнен!")
            result_joke.encoding = 'utf-8'
            print(result_joke.text)
            check = result_joke.json()
            check_info_value = check.get("value")
            print(check_info_value)


category_joke = Test_joke()
category_joke.test_get_joke_from_categories()