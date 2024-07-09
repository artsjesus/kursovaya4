import json
from abc import ABC, abstractmethod


class FileWork(ABC):

    @abstractmethod
    def read_file(self):
        pass

    @abstractmethod
    def save_file(self):
        pass


class WorkWithJson(FileWork):

    def read_file(self):
        with open("data/vacancies.json", "r", encoding="utf-8") as file:
            return json.load(file)

    def save_file(self, data):
        with open("data/vacancies.json", "w", encoding="utf-8") as file:
            json.dump(data, file,  ensure_ascii=False, indent=4)

    @staticmethod
    def get_data(criterion):
        """Метод получения данных из файла по указанным критериям"""
        criterion_vac = []
        with open("data/vacancies.json", "r", encoding="utf8") as file:
            vacancies = json.load(file)
            for vac in vacancies:
                if not vac["snippet"]["requirement"]:
                    continue
                else:
                    if criterion in vac["snippet"]["requirement"]:
                        criterion_vac.append(vac)
        return criterion_vac
