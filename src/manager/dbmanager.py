import csv
from abc import ABC, abstractmethod

import psycopg2


class Manager(ABC):
    """
    класс работы с sql запросами
    """

    @abstractmethod
    def create_database(self) -> None:
        """
        Создает базу данных.
        Принимает параметры создаваемой базы в формате:
        {
        'host': 'localhost'
        'user': 'user'
        'password': 'password'
        'port': '5432'
        }
        Название БД = name
        :return: None
        """
        pass

    @abstractmethod
    def execute_sql_script(self) -> None:
        """
        Реализует sql скрипт.
        В name передаем название базы данных.
        В params передаем пераметры:
        {
        'host': 'localhost'
        'user': 'user'
        'password': 'password'
        'port': '5432'
        }
        В path передаем путь до sql файла с реализуемым скриптом
        :return: None
        """
        pass

    @abstractmethod
    def insert_employers_data(self) -> None:
        """
        Записывает данные employers.csv
        в таблицу базы данных kw5
        :return: None
        """
        pass



class DBManager(Manager, ABC):
    def __init__(self,
                 name: str,
                 params: dict,
                 sql_path: str,
                 csv_path: str,
                 csv_path_vacancy: str
                 ):
        self.name = name
        self.params = params
        self.sql_path = sql_path
        self.csv_path = csv_path
        self.csv_path_vacancy = csv_path_vacancy
        self.conn = psycopg2.connect(dbname='postgres', **self.params)
        self.cur = self.conn.cursor()


    def create_database(self) -> None:
        self.conn.autocommit = True
        self.cur.execute(f'CREATE DATABASE {self.name}')


    def execute_sql_script(self) -> None:
        conn = psycopg2.connect(dbname=self.name, **self.params)
        with open(self.sql_path, 'r', encoding='utf-8') as file:
            sql_script = file.read()
            try:
                with conn:
                    with conn.cursor() as cur:
                        cur.execute(sql_script)
            finally:
                conn.close()

    def insert_employers_data(self) -> None:
        conn = psycopg2.connect(dbname=self.name, **self.params)
        try:
            with conn:
                with conn.cursor() as cur:
                    with open(self.csv_path, 'r', newline='') as file:
                        employers = csv.reader(file)
                        next(employers)
                        for employer in employers:
                            cur.execute(
                                "INSERT INTO employers (employers_id, company_name, open_vacancies, vacancies_url)"
                                " VALUES (%s,%s, %s, %s)",
                                employer[:4])
        finally:
            conn.close()

    def insert_vacancy_data(self, name: str) -> None:
        conn = psycopg2.connect(dbname=self.name, **self.params)
        try:
            with conn:
                with conn.cursor() as cur:
                    with open(self.csv_path_vacancy/f"{name}.csv", 'r', newline='') as file:
                        vacancies = csv.reader(file)
                        next(vacancies)
                        for vacancy in vacancies:
                            cur.execute(
                                "INSERT INTO vacancies (company_name, vacancy_id, vacancy_name, salary_from, "
                                "salary_from, vacancies_url)"
                                " VALUES (%s,%s, %s, %s, %s, %s)",
                                vacancy)
        finally:
            conn.close()
