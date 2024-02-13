from pathlib import Path


from configparser import ConfigParser


CSV_PATH = Path.joinpath(Path(__file__).parent, "employers", "employers.csv")
CSV_PATH_VACANCIES = Path.joinpath(Path(__file__).parent, "vacancies")
SQL_PATH = Path.joinpath(Path(__file__).parent, "fill_table.sql")




def config(filename="database.ini", section="postgresql"):
    # create a parser
    parser = ConfigParser()
    # read config file
    parser.read(filename)
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception(
            'Section {0} is not found in the {1} file.'.format(section, filename))
    return db
