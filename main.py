from src.parser import HH
from src.utils import vac_user, sorting
from src.creat_bd import WorkWithJson


def main():
    user_vacancy = input('Введите вакансию для поиска на сайте hh.ru: \n')
    hh = HH(user_vacancy)
    hh.load_vacancies()
    vacancies = hh.vacancies
    fv = WorkWithJson()
    fv.save_file(vacancies)
    name_criterion = input('Введите критерий для отбора вакансий: \n')
    fv.get_data(name_criterion)
    processed_vacancies = vac_user()
    n = input('Введите количество вакансий для просмотра: \n')
    top_vacancies = sorting(processed_vacancies, int(n))
    for vac in top_vacancies:
        print(vac)


if __name__ == '__main__':
    main()
