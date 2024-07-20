import json
from abc import ABC, abstractmethod


class FileWork(ABC):

    @abstractmethod
    def read_file(self):
        """чтение файла"""
        pass

    @abstractmethod
    def save_file(self, datae):
        """сохранения файла"""
        pass

    @abstractmethod
    def del_file(self):
        """удаление"""
        pass


class WorkWithJson(FileWork):
    def __init__(self, file_name):
        self.file_name = file_name

    def read_file(self):
        with open(f"data/{self.file_name}", "r", encoding="utf-8") as file:
            return json.load(file)

    def save_file(self, data):
        """Добавляет новые данные в JSON файл."""
        with open(f"data/{self.file_name}", 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    def del_file(self):
        with open(f"data/{self.file_name}", "w") as file:
            pass

    def get_data(self, criterion):
        """Метод получения данных из файла по указанным критериям"""
        criterion_vac = []
        with open(f"data/{self.file_name}", "r", encoding="utf8") as file:
            vacancies = json.load(file)
            for vac in vacancies:
                if not vac["snippet"]["requirement"]:
                    continue
                else:
                    if criterion in vac["snippet"]["requirement"]:
                        criterion_vac.append(vac)
        return criterion_vac
