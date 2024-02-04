from abc import ABC, abstractmethod

import requests


class API(ABC):
    """
    Абстрактный API класс c методом запроса
    """

    @abstractmethod
    def get_employers(self, employer_id: int) -> list[dict]:
        raise NotImplementedError


class HeadHunterAPI(API, ABC):
    """
    API класс ресурса HeadHunter
    """
    def get_employers(self, employer_id: int) -> list[dict]:
        """
        Метод запроса данных с HeadHunter employers
        с проверкой на доступность данных.
        :return: json
        """
        response = requests.get(f'https://api.hh.ru/employers/{employer_id}')
        if response.status_code != 200:
            raise RecursionError(f'{response.status_code}')
        else:
            return response.json()
