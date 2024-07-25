from src.vacancies import JobVacancy
from src.creat_bd import WorkWithJson
from src.parser import CB


def creat_class(file_name):
    """Создание класса"""
    list_vacancies = []
    cb = CB()
    cb.load_vacancies()
    vacancies = WorkWithJson(file_name)
    for vac in vacancies.read_file():
        if not vac["salary"]:
            vac["salary"] = {"from": 0, "to": 0, "currency": ""}
        vacancy = JobVacancy(vac['name'], vac['salary'], vac['url'], vac["snippet"]['requirement'])
        vacancy.well(cb)
        list_vacancies.append(vacancy)
    return list_vacancies


def sorting(vacancies, criterion, n: int):
    """Сортировка N вакансий и поиск по ключевым словам"""
    criterion_vacancies = []
    for vac in vacancies:
        if not vac.requirement:
            continue
        else:
            if criterion in vac.requirement:
                criterion_vacancies.append(vac)
    criterion_vacancies = sorted(vacancies, reverse=True)
    return criterion_vacancies[:n]
