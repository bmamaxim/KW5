
from abc import ABC, abstractmethod


from config import CSV_PATH, CSV_PATH_VACANCIES

import re


class Saver(ABC):
    """
    Класс с методами записи, читения, сохранения
    json данных по по работодателям, переданны из "main"
    """
    @abstractmethod
    def add_employers(self, employers: list) -> None:
        """
        Метод записи в файл, по заданному пути: "CSV_PATH",
        данных по работодателям переданных из "main"
        employers - json данные о работодателях
        из внешнего источника (HH.ru)
        :param employers: list
        :return: None
        """
        raise NotImplemented

    @abstractmethod
    def add_vacancies(self, name: str, vacancies_url: str) -> None:
        """
        Метод записи в файл, по заданному пути: "CSV_PATH",
        данных по вакансиям работодателей переданных из "main"
        title - ключ название профессии из файла employers.json
        vacancies_url - ключ url ссылка на вакансию из файла employers.json
        :param name: str
        :param vacancies_url: str
        :return: None
        """
        raise NotImplemented

class CSVSaver(Saver, ABC):
    """
    Класс записи локальных файлов
    """

    def add_employers(self, employers: list) -> None:
        employer = [employer.to_dict_employer() for employer in employers]
        output = ('"' + '","'.join([*employer[0]]) + '"')
        for obj in employer:
            output += (f"\n{obj['employers_id']},"
                       f"{obj['company_name'].replace(',', "")},"
                       f"{obj['open_vacancies']},"
                       f"{obj['vacancies_url']},"
                       )
        with open(CSV_PATH, 'w', newline='') as file:
            file.write(output)

    def add_vacancies(self, name: str, vacancies: list,) -> None:
        vacancy = ""
        vacancy += (f"\n{name.replace(',', "")},"
                    f"{vacancies['vacancy_id']},"
                    f"{re.sub('[(|)|,]', '', vacancies['vacancy_name'])},"
                    f"{vacancies['salary']['from']},"
                    f"{vacancies['salary']['to']},"
                    f"{vacancies['vacancies_url']}")
        with open(CSV_PATH_VACANCIES, 'a', encoding='utf-8') as file:
            file.write(vacancy)
