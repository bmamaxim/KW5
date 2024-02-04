import json
from abc import ABC, abstractmethod

from config import JSON_PATH


class Saver(ABC):
    """
    Класс с методами записи, читения, сохранения
    json данных по по работодателям, переданны из "main"
    """
    @abstractmethod
    def add_vacancy(self, vacancies: list) -> None:
        """
        Метод записи в файл, по заданному пути: "JSON_PATH",
        данных по вакансиям переданных из "main"
        :param vacancies: list
        :return: None
        """
        raise NotImplemented


class JSONSaver(Saver):

    def add_vacancy(self, employers: list) -> None:
        employer = [employer.to_dict_employer() for employer in employers]
        with open(JSON_PATH, 'w', encoding='utf-8') as file:
            json.dump(employer, file)
