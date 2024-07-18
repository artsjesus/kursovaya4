from src.parser import HH
from src.utils import vac_user, sorting
from src.creat_bd import WorkWithJson


def main():
    file_name = input("Введите имя фала:\n") + ".json"
    user_vacancy = input('Введите вакансию для поиска на сайте hh.ru: \n')
    hh = HH(user_vacancy)
    if hh.connect != 200:
        print(f"Ошибка: {hh.connect}")
    else:
        hh.load_vacancies()
        vacancies = hh.vacancies
        fv = WorkWithJson(file_name)
        fv.save_file(vacancies)
        name_criterion = input('Введите критерий для отбора вакансий: \n')
        fv.get_data(name_criterion)
        processed_vacancies = vac_user(file_name)
        n = input('Введите количество вакансий для просмотра: \n')
        top_vacancies = sorting(processed_vacancies, int(n))
        for vac in top_vacancies:
            print(vac)
        delete = input("Удалить список вакансий?(Y/N)").upper()
        if delete == "Y":
            fv.del_file()


if __name__ == '__main__':
    main()
