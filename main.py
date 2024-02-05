from config import JSON_PATH
from src.data_processing.engine import HeadHunterAPI
from src.data_record.save import JSONSaver
from src.utils import hh_inst_employer, reading_file, hh_inst_vacancies


def user_interaction():
    """
    Мейн функция:
    связывает все классы и объекты программы
    :return: sql
    """
    # id рботодателей
    employers_id = [2180, 9498112, 4598057, 41862, 3968, 10325037, 10309, 982698, 49357, 1942330]
    hirer = HeadHunterAPI()
    employers = []
    for employer_id in employers_id:
        employers.append(hirer.get_employers(employer_id))
    employers_init = hh_inst_employer(employers)
    json_saver = JSONSaver()
    json_saver.add_employers(employers_init)
    for employer in employers:
        employer_vacancies = hirer.get_vacancies(employer['vacancies_url'])
        vacancies_init = hh_inst_vacancies(employer_vacancies)

        for employ in reading_file(JSON_PATH):
            json_saver.add_vacancies(employ["title"], vacancies_init)


if __name__ == "__main__":
    user_interaction()