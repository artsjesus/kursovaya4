from src.vacancies import JobVacancy
import json


def vac_user():
    """Приводит полученные данные к данным для вывода"""

    with open("data/vacancies.json", "r", encoding="utf8") as f:
        vacancies = json.load(f)
    user_vac = []
    for vac in vacancies:
        if not vac.get("salary"):
            vac["salary"] = {"from": 0, "to": 0, "currency": ""}
        else:
            if vac["salary"] is None or not isinstance(vac["salary"], dict):
                vac["salary"] = {"from": 0, "to": 0, "currency": ""}
            else:
                if vac["salary"]["currency"] is None:
                    vac["salary"]["currency"] = "Валюта не определена"

                if vac["salary"]["from"] is None:
                    vac["salary"]["from"] = 0
                if vac["salary"]["to"] is None:
                    vac["salary"]["to"] = 0

        vac["snippet"]["requirement"] = vac["snippet"].get("requirement", "Информация отсутствует")
        user_vac.append(vac)

    return user_vac


def sorting(vacancies, n: int):
    sort_vac = []
    for vac in vacancies:
        try:
            pass
            sort_vac.append(JobVacancy(vac['name'], vac['salary'], vac['url'], vac["snippet"]['requirement']))
        except TypeError as e:
            print(f"Ошибка при обработке вакансии: {vac}")
            print(e)
            continue

    sorted_vacancies = sorted(sort_vac, key=lambda x: x.salary["to"], reverse=True)
    return sorted_vacancies[:n]
