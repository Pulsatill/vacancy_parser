from abc import abstractmethod, ABC
import requests
import json
import os

from requests import Response


class Engine(ABC):
    @abstractmethod
    def get_request(self, url, params):
        try:
            response = requests.get(url=url, params=params)
            return response
        except ConnectionError:
            print(f'На данный момент не могу подключиться к серверу.')

    @staticmethod
    def get_connector(file_name):
        """ Возвращает экземпляр класса Connector """
        pass


class HeadHunter(Engine):
    def __init__(self):
        self.url = "https://api.hh.ru/"
        self.params = None

    def get_request(self):
        return super().get_request(self.url, self.params)


class SuperJob(Engine):
    def __init__(self):
        self.url = "https://russia.superjob.ru/vacancy/search/"
        self.word = None
        self.page = None
        self.town = None
        self.params = {'town': {self.town},
                       'keywords': {self.word},
                       'page': {self.page},
                       'count': 20,
                       'order_field': 100000,
                       'no_agreement': 0}

    def get_request(self) -> tuple:
        sj_api = {'X-Api-App-Id': os.environ['API_SuperJob']}
        response = requests.get('https://api.superjob.ru/2.0/vacancies/',
                                headers=sj_api,
                                params=self.params)
        data = response.json()
        return data


class RabotaRu(Engine):
    def __init__(self):
        self.url = "https://opendata.trudvsem.ru/api/v1/vacancies"
        self.params = None

    def get_request(self):
        return super().get_request(self.url, self.params)


class TrudVsem(Engine):
    def __init__(self):
        self.url = "https://opendata.trudvsem.ru/api/v1/vacancies"
        self.params = None

    def get_request(self) -> tuple:
        response = super().get_request(self.url, self.params)
        data = response.json()
        return data


tv = TrudVsem()
print(tv.get_request())
#
# retro = requests.get("https://api.hh.ru/")
# print(retro)

# sj = SuperJob()
# print(sj.get_request())
