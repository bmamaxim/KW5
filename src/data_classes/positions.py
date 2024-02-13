

class Employer:
    """
    Класс информации о работодателях
    """
    def __init__(self,
                 pk: int,
                 name: str,
                 vacancies: int,
                 employer_url: str,
                 vacancies_url: str
                 ) -> object:
        self.__pk = pk
        self.__name = name
        self.__vacancies = vacancies
        self.__employer_url = employer_url
        self.__vacancies_url = vacancies_url

    def to_dict_employer(self) -> dict:
        """
        Метод стандартизируемой записи данных
        работодателя для .json
        :return: dict
        """
        return {
            'employers_id': self.__pk,
            'company_name': self.__name,
            'open_vacancies': self.__vacancies,
            'vacancies_url': self.__vacancies_url
        }


class Vacancies:
    """
    Класс вакансий работодателя
    """
    def __init__(self,
                 pk: int,
                 title: str,
                 salary: int,
                 vacancies_url: str
                 ) -> object:
        self.__pk = pk
        self.__title = title
        self.__salary = salary
        self.__vacancies_url = vacancies_url
        self.validate_salary()

    def validate_salary(self):
        """
        Метод валидатор, проверяет salary,
        возвращает доступное значение.
        :return: int
        """
        if self.__salary and isinstance(self.__salary, dict):
            from_ = self.__salary["from"]
            to = self.__salary["to"]
            self.__salary["from"] = from_ if from_ else 0
            self.__salary["to"] = to if to else 0
        else:
            self.__salary = {
                "from": 0,
                "to": 0,
            }

    def to_dict_vacancy(self) -> dict:
        """
        Метод стандартизируемой записи данных
        по вакансиям работодателей
        :return: dict
        """
        return {
            'vacancy_id': self.__pk,
            'vacancy_name': self.__title,
            'salary': self.__salary,
            'vacancies_url': self.__vacancies_url
        }
