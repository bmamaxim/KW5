import json
from abc import ABC, abstractmethod

from config import JSON_PATH, JSON_PATH_VACANCIES


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
        :param employers: list
        :return: None
        """
        raise NotImplemented

    @abstractmethod
    def add_vacancies(self, title: str, vacancies_url: str) -> None:
        """
        Метод записи в файл, по заданному пути: "JSON_PATH",
        данных по вакансиям работодателей переданных из "main"
        :param title: str
        :param vacancies_url: str
        :return: None
        """
        raise NotImplemented

class JSONSaver(Saver, ABC):
    """
    Класс записи json данных
    """

    def add_employers(self, employers: list) -> None:
        """
        Функция записи json данных о работодателях
        по заранее записанному пути
        :param employers: list
        :return: list[dict]
        """
        employer = [employer.to_dict_employer() for employer in employers]
        with open(JSON_PATH, 'w', encoding='utf-8') as file:
            json.dump(employer, file)

    def add_vacancies(self, title: str, vacancies: list,) -> None:
        """
        Функция записи json данных по вакансиям
        заранее определенных работодателей
        :param title: str
        :param vacancies:
        :return:
        """
        vacancy = [vacancy.to_dict_vacancy() for vacancy in vacancies]
        with open(JSON_PATH_VACANCIES/f"{title}.json", 'w', encoding='utf-8') as file:
            json.dump(vacancy, file)