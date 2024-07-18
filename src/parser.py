import requests
from abc import ABC, abstractmethod


class Parser(ABC):
    @abstractmethod
    def load_vacancies(self, **kwargs):
        pass


class HH(Parser):
    """
    Класс для работы с API HeadHunter
    Класс Parser является родительским классом, который вам необходимо реализовать
    """

    def __init__(self, keyword: str):
        self.url = 'https://api.hh.ru/vacancies'
        self.__headers = {'User-Agent': 'HH-User-Agent'}
        self.params = {'text': keyword, 'page': 0, 'per_page': 100}
        self.vacancies = []

    def load_vacancies(self, **kwargs):
        while self.params.get('page') != 5:
            response = requests.get(self.url, headers=self.__headers, params=self.params)
            vacancies = response.json()['items']
            self.vacancies.extend(vacancies)
            self.params['page'] += 1

    @property
    def connect(self):
        return requests.get(self.url).status_code


class CB(Parser):
    def __init__(self):
        self.__url = "https://www.cbr-xml-daily.ru/daily_json.js"
        self.Exchange = dict

    def load_vacancies(self, **kwargs):
        response = requests.get(self.__url)
        self.Exchange = response.json()['Valute']

    @property
    def show_exchange(self):
        return self.Exchange

    def __str__(self):
        return f"{CB.__class__.__name__}({self.Exchange})"
