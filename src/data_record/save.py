import json
from abc import ABC, abstractmethod
from typing import List, Any

from config import CSV_PATH, CSV_PATH_VACANCIES


class Saver(ABC):
    """
    Класс с методами записи, читения, сохранения
    json данных по по работодателям, переданны из "main"
    """
    @abstractmethod
    def add_employers(self, employers: list) -> None:
        """
        Метод записи в файл, по заданному пути: "JSON_PATH",
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
        Метод записи в файл, по заданному пути: "JSON_PATH",
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
        print(employer)
        output = ('"' + '","'.join([*employer[0]]) + '"')
        print(output)
        for obj in employer:
            print(obj)
            output += (f"\n{obj['employers_id']},"
                       f"{obj['company_name']},"
                       f"{obj['open_vacancies']},"
                       f"{obj['vacancies_url']}")
        with open(CSV_PATH, 'w', newline='') as file:
            file.write(output)

    def add_vacancies(self, name: str, vacancies: list,) -> None:
        vacancy = [vacancy.to_dict_vacancy() for vacancy in vacancies]
        output = ','.join([*vacancy[0]])
        print(output)
        for obj in vacancy:
            output += (f"\n{name},"
                       f"{obj['vacancy_id']},"
                       f"{obj['vacancy_name']},"
                       f"{obj['salary']['from']},"
                       f"{obj['salary']['to']},"
                       f"{obj['vacancies_url']}")
        with open(CSV_PATH_VACANCIES/f"{name}.csv", 'w', encoding='utf-8') as file:
            file.write(output)
