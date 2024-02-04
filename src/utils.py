from src.data_classes.positions import Employer, Vacancies


def hh_inst_employer(data):
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
                        title=info['name'],
                        vacancies=info['open_vacancies'],
                        employer_url=info['alternate_url'],
                        vacancies_url=info['vacancies_url']
            ))
        return employer_info


def hh_inst_vacancies(data):
    """
    Инициализируем класс Vacancies
    :param data: json
    :return: list[dikt]
    """
    vacancies_info = []
    if data:
        for info in data:
            vacancies_info.append(Vacancies(
                        pk=info['id'],
                        title=info['name'],
                        salary_from=info.get('salary')['from'],
                        salary_to=info.get('salary')['to'],
                        vacancies_url=info['alternate_url']
            ))
        return vacancies_info