class JobVacancy:
    def __init__(self, name: str, salary: dict, url: str, requirement: str):
        if not isinstance(salary, dict):
            raise TypeError("Salary must be a dictionary")
        self.name = name
        self.salary = salary
        self.url = url
        self.requirement = requirement

    def __str__(self):
        return (
            f"Название: {self.name}\n"
            f"Зарплата: от {self.salary['from']} до {self.salary['to']} {self.salary['currency']}\n"
            f"Ссылка: {self.url}\n"
            f"Требования: {self.requirement}\n"
        )

    def validation(self):
        if not self.salary:
            self.salary = {"from": 0, "to": 0, "currency": ""}
        else:
            if self.salary is None or not isinstance(self.salary, dict):
                self.salary = {"from": 0, "to": 0, "currency": ""}
            else:
                if self.salary["currency"] is None:
                    self.salary["currency"] = "Валюта не определена"

                if self.salary["from"] is None:
                    self.salary["from"] = 0
                if self.salary["to"] is None:
                    self.salary["to"] = 0

    def well(self, cb):
        if self.salary["currency"] != "RUR" and self.salary["currency"] != "" and "BYR" != self.salary["currency"]:
            currency = self.salary["currency"]
            self.salary["from"] = round(self.salary["from"] * cb.Exchange[currency]["Value"] / cb.Exchange[currency]["Nominal"])
            self.salary["to"] = round(self.salary["to"] * cb.Exchange[currency]["Value"] / cb.Exchange[currency]["Nominal"])
            self.salary["currency"] = f"RUR, выплата в {currency}"

    def __repr__(self):
        return f"{JobVacancy.__class__.__name__}({self.name}, {self.salary}, {self.url}, {self.requirement})"

    def __gt__(self, other):
        return self.salary['to'] > other.salary['to']

    def __lt__(self, other):
        return self.salary['to'] < other.salary['to']
