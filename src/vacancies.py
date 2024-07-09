class JobVacancy:
    def __init__(self, name: str, url: str, salary: dict, description: str):
        if not isinstance(salary, dict):
            raise TypeError("Salary must be a dictionary")
        self.name = name
        self.url = url
        self.salary = salary
        self.description = description

    def __gt__(self, other):
        return self.salary['to'] > other.salary['to']

    def __str__(self):
        return (
            f"Название: {self.name}\n"
            f"Зарплата: от {self.salary} до {self.salary['to']} {self.salary}\n"
            f"Ссылка: {self.url}\n"
            f"Требования: {self.description}\n"
        )

    def __repr__(self):
        return f"Vacancy({self.name}, {self.salary}, {self.url}, {self.description})"