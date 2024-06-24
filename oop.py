class students:
    # constructor
    def __init__(self, first_name, last_name,):
        self.first_name = first_name
        self.last_name = last_name

    #method
    def display(self):
        print(self.first_name, self.last_name)


# object
my_students = students("Kimanthi", "Muinde")
my_students.display()
my_students2 = students("Justus", "Muinde")
my_students2.display()
my_students3 = students("Tiff", "Muinde")
my_students3.display()
my_students4 = students("Blessi", "Muinde")
my_students4.display()
my_students5 = students("Peshy", "Muinde")
my_students5.display()