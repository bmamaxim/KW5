from src.data_processing.engine import HeadHunterAPI
from src.data_record.save import JSONSaver
from src.utils import hh_inst_employer


def user_interaction():
    """
    Мейн функция:
    связывает все классы и объекты программы
    :return: sql
    """
    # id рботодателей
    employers_id = [2180, 9498112, 4598057, 41862, 3968, 10325037, 10309, 982698, 49357, 1942330]
    employers =[]
    for employer_id in employers_id:
        hirer = HeadHunterAPI()
        employers.append(hirer.get_employers(employer_id))
    employers_init = hh_inst_employer(employers)
    json_saver = JSONSaver()
    json_saver.add_vacancy(employers_init)


if __name__ == "__main__":
    user_interaction()