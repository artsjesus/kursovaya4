from src.vacancies import JobVacancy
from src.creat_bd import WorkWithJson
from src.parser import CB



def vac_user(file_name):
    """Приводит полученные данные к данным для вывода"""
    vacancies = WorkWithJson(file_name)
    user_vac = []
    for vac in vacancies.read_file():
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
    """Сортировка N вакансий"""
    sort_vac = []
    cb = CB()
    cb.load_vacancies()
    for vac in vacancies:
        try:
            if vac["salary"]["currency"] != "RUR" and vac["salary"]["currency"] != "" and "BYR" != vac["salary"][
                "currency"]:
                currency = vac["salary"]["currency"]
                vac["salary"]["from"] = round(
                    vac["salary"]["from"] * cb.Exchange[currency]["Value"] / cb.Exchange[currency]["Nominal"])
                vac["salary"]["to"] = round(
                    vac["salary"]["to"] * cb.Exchange[currency]["Value"] / cb.Exchange[currency]["Nominal"])
                vac["salary"]["currency"] = f"RUR, выплата в {currency}"
            sort_vac.append(JobVacancy(vac['name'], vac['salary'], vac['url'], vac["snippet"]['requirement']))

        except TypeError as e:
            print(f"Ошибка при обработке вакансии: {vac}")
            print(e)
            continue
    #sort_vac = sorted(sort_vac["to"])
    sort_vac = sorted(sort_vac, reverse=True)
    return sort_vac[:n]
