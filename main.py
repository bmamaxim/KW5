from config import CSV_PATH, config, SQL_PATH
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
    # id рботодателей
    employers_id = [2180, 9498112, 4598057, 41862, 3968, 10325037, 10309, 982698, 49357, 1942330]

    # создание базы данных
    name = 'kw5'
    params = config()
    bd_manager = DBManager(name, params, SQL_PATH, CSV_PATH)
    bd_manager.create_database()

    hirer = HeadHunterAPI()
    employers = []
    for employer_id in employers_id:
        employers.append(hirer.get_employers(employer_id))
    employers_init = hh_inst_employer(employers)
    csv_saver = CSVSaver()
    csv_saver.add_employers(employers_init)
    for employer in employers:
        employer_vacancies = hirer.get_vacancies(employer['vacancies_url'])
        vacancies_init = hh_inst_vacancies(employer_vacancies)
        csv_saver.add_vacancies(employer["name"], vacancies_init)
    bd_manager.execute_sql_script()
    bd_manager.insert_employers_data()


if __name__ == "__main__":
    user_interaction()