from src.data_classes.positions import Employer, Vacancies


def hh_inst_employer(data: dict) -> object:
    """
    Инициализируем класс Employer
    :param data: json
    :return: list[dikt]
    """
    employer_info = []
    if data:
        for info in data:
            employer_info.append(Employer(
                        pk=info['id'],
                        name=info['name'],
                        vacancies=info['open_vacancies'],
                        employer_url=info['alternate_url'],
                        vacancies_url=info['vacancies_url']
            ))
        return employer_info


def hh_inst_vacancies(data: dict) -> object:
    """
    Инициализируем класс Vacancies
    :param data: json
    :return: list[dikt]
    """
    vacancies_info = []
    if data:
        for info in data['items']:
            vacancies_info.append(Vacancies(
                        pk=info['id'],
                        title=info['name'],
                        salary=info.get('salary'),
                        vacancies_url=info['alternate_url']
            ))
        return vacancies_info


def reading_file(path: str, name: str) -> list[dict]:
    """
    Функция чтения json файла.
    В path передаем путь до файла, который читаем
    :param name: str
    :param path: str
    :return: json
    """
    with open(path/f"{name}.csv", 'r', encoding='utf-8') as file:
        return file.read()

def add_structure(paht: str, name: str) -> None:
    output = "company_name,vacancy_id,vacancy_name,salary_from,salary_to,vacancies_url"
    with open(paht/f"{name}", 'w', newline='') as file:
        file.write(output)