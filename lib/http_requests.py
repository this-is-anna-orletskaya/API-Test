import requests
from logger import Logger



"""Модуль основных HTTP запросов на основе библиотеки requests с включением логирования"""


class HttpMethods():

    # headers = {'Content-Type': 'application/json'}
    # cookies = ""

    @staticmethod
    def get(url, headers):
        Logger.add_request(url, method="GET")
        response = requests.get(url, headers=headers)
        Logger.add_response(response)
        return response
    
    @staticmethod
    def post(url, headers, body):
        Logger.add_request(url, method="POST")
        response = requests.post(url, headers=headers, json=body)
        Logger.add_response(response)
        return response
    
    @staticmethod
    def put(url, headers, body):
        Logger.add_request(url, method="PUT")
        response = requests.put(url, headers=headers, json=body)
        Logger.add_response(response)
        return response 
    
    @staticmethod
    def delete(url, headers):
        Logger.add_request(url, method="DELETE")
        response = requests.delete(url, headers=headers)
        Logger.add_response(response)
        return response 