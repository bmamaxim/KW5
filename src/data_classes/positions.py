

class Employer:
    """
    Класс информации о работодателях
    """
    def __init__(self,
                 pk: int,
                 title: str,
                 vacancies: int,
                 employer_url: str,
                 vacancies_url: str
                 ) -> object:
        self.__pk = pk
        self.__title = title
        self.__vacancies = vacancies
        self.__employer_url = employer_url
        self.__vacancies_url = vacancies_url

    def to_dict_employer(self):
        """
        Метод стандартизируемой записи данных
        работодателя для .json
        :return:
        """
        return {
            'id': self.__pk,
            'title': self.__title,
            'open_vacancies': self.__vacancies,
            'employer_url': self.__employer_url,
            'vacancies_url': self.__vacancies_url
        }


class Vacancies:
    """
    Класс вакансий работодателя
    """
    def __init__(self,
                 pk: int,
                 title: str,
                 salary_from: int,
                 salary_to: int,
                 vacancies_url: str
                 ) -> object:
        self.__pk = pk
        self.__title = title
        self.__salary_from = salary_from if salary_from else 0
        self.__salary_to = salary_to if salary_to else 0
        self.__vacancies_url = vacancies_url

    def to_dict_vacancy(self):
        """
        Метод стандартизируемой записи данных
        по вакансиям работодателей
        :return:
        """
        return {
            'id': self.__pk,
            'title': self.__title,
            'salary_from': self.__salary_from,
            'salary_to': self.__salary_to,
            'vacancies_url': self.__vacancies_url
        }
