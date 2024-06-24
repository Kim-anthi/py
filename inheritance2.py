class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def print_name(self):
        print(f"My name is {self.first_name} {self.last_name}, and I am {self.age} years old.")


class Students(Person):
    def __init__(self, first_name, last_name, age,):

        super().__init__(first_name, last_name, age)


myStudent = Students("John", "Doe", 29)
myStudent.print_name()
myStudent = Students("Kate", "Meghan", 26)
myStudent.print_name()
myStudent = Students("James", "Brown", 34)
myStudent.print_name()
myStudent = Students("Vee", "Markhle", 39)
myStudent.print_name()
