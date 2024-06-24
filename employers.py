class Employees:
    def __init__(self, name, ID, salary):
        self.name = name
        self.ID = ID
        self.salary = salary

    def display_info(self):
        print(f"Name:{self.name}")
        print(f"ID:{self.ID}")
        print(f"Salary:{self.salary}")

    def calculate_salary(self):
        print(f"Annual Salary is: {self.salary * 12}")


class Manager(Employees):
    def __init__(self, name, ID, salary, department, List_of_employees):
        super().__init__(name, ID, salary)
        self.department = department
        self.list_of_employees = List_of_employees

        print(f"Name:{self.name}")
        print(f"ID:{self.ID}")
        print(f"Salary:{self.salary}")
        print(f"List_of_employees:{self.list_of_employees}")

    def calculate_salary(self):
        print(f"The Annual Salary is:{self.salary * 12}")


class Developers(Employees):
    def __init__(self, name, ID, salary, List_of_programming_languages):
        super().__init__(name, ID, salary)
        self.List_of_programming_languages = List_of_programming_languages
        self.List_of_programming_languages.append(List_of_programming_languages)

    def display_info(self):
        print(f"List of Programming languages{self.List_of_programming_languages}")

    def add_skill(self, language):
        self.List_of_programming_languages.append(language)

    def calculate_salary(self):
        print(f"The Annual Salary is:{self.salary * 12}")


class Interns(Employees):
    def __init__(self, name, ID, salary, school_name, graduation_year):
        super().__init__(name, ID, salary)
        self.school_name = school_name
        self.graduation_year = graduation_year
        print(f"Name:{self.name}")
        print(f"ID:{self.ID}")
        print(f"Salary:{self.salary}")
        print(f"school_name:{self.school_name}")
        print(f"graduation_year:{self.graduation_year}")

    def calculate_salary(self):
        print(f"The Annual Salary is:{self.salary * 12}")


employee = Employees("Kim", 1001, 100000)
employee.display_info()
employee.calculate_salary()
develop = Developers("Kim", 1001, 100000, [])
develop.display_info()
develop.calculate_salary()
develop.add_skill("php")
develop.display_info()
