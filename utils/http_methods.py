import requests

"""Список HTTP-методов"""

class HttpMethods:
    headers = {'Content-Type' : 'application/json'}
    cookie = {"cookie_name": "cookie_value"}

    @staticmethod
    def get(url):
        result = requests.get(url, headers=HttpMethods.headers, cookies=HttpMethods.cookie)
        return result

    @staticmethod
    def post(url, body):
        result = requests.post(url, headers=HttpMethods.headers, cookies=HttpMethods.cookie, json=body)
        return result

    @staticmethod
    def put(url, body):
        result = requests.put(url, headers=HttpMethods.headers, cookies=HttpMethods.cookie, json=body)
        return result

    @staticmethod
    def delete(url, body):
        result = requests.delete(url, headers=HttpMethods.headers, cookies=HttpMethods.cookie, json=body)
        return result