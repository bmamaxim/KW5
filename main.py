import psycopg2

from config import CSV_PATH, config, SQL_PATH, CSV_PATH_VACANCIES
from src.manager.dbmanager import DBManager
from src.data_processing.engine import HeadHunterAPI
from src.data_record.save import CSVSaver
from src.utils import hh_inst_employer, hh_inst_vacancies


def user_interaction():
    """
    Мейн функция:
    связывает все классы и объекты программы
    :return: sql
    """
    print("привет")
    # id рботодателей
    employers_id = [2180, 9498112, 4598057, 41862, 3968, 10325037, 10309, 982698, 49357, 1942330]

    # создание базы данных
    name = 'kw5'
    params = config()
    bd_manager = DBManager(name, params, SQL_PATH, CSV_PATH, CSV_PATH_VACANCIES)
    bd_manager.create_database()
    bd_manager.execute_sql_script()
    hirer = HeadHunterAPI()
    employers = []
    for employer_id in employers_id:
        employers.append(hirer.get_employers(employer_id))
    employers_init = hh_inst_employer(employers)
    csv_saver = CSVSaver()
    csv_saver.add_employers(employers_init)
    bd_manager.insert_employers_data()
    for employer in employers:
        employer_vacancies = hirer.get_vacancies(employer['vacancies_url'])
        vacancies_init = hh_inst_vacancies(employer_vacancies)
        csv_saver.add_vacancies(employer["name"], vacancies_init)
        bd_manager.insert_vacancy_data(employer["name"])

    company_vacancy = input("вывести компании и количество вакансий?\n"
                            "если 'да' нажмите любой символ и enter"
                            "если пропустить запрос 'enter'\n")
    if company_vacancy:
        for exe in bd_manager.get_companies_and_vacancies_count():
            print(exe)
        else:
            pass


    all_vacancy = input("вывести все вакансии (400шт)\n"
                        "если 'да' нажмите любой символ и enter"
                        "если пропустить запрос 'enter'\n")
    if all_vacancy:
        for exe in bd_manager.get_all_vacancies():
            print(exe)
        else:
            pass

    print(f"Средняя зарплата по вакансиям: \n"
          f"{int(bd_manager.get_avg_salary()[0][0])}")

    query = input("поиск по слову в вакансиях\n"
                  "введите слово:\n")
    if query:
        for exe in bd_manager.get_vacancies_with_keyword(query.title()):
            print(exe)
        else:
            pass
          

if __name__ == "__main__":
    user_interaction()
