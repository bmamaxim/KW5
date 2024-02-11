
--
-- Name: employers; Type: TABLE; Schema: public; Owner: -; Tablespace:
--

CREATE TABLE employers (
    employers_id int NOT NULL,
    company_name text,
    open_vacancies text,
    vacancies_url text
);

--
-- Name: vacancies; Type: TABLE; Schema: public; Owner: -; Tablespace:
--

CREATE TABLE vacancies (
    company_name text,
    vacancy_id int NOT NULL,
    vacancy_name text,
    salary_from int,
    salary_to int,
    vacancies_url text
);