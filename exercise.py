class cars:
    def __init__(self, model, year, type, color):
        self.model = model
        self.year = year
        self.type = type
        self.color = color

    def cars(self):
        print(f"My dream car is {self.model} manufactured in {self.year} being a {self.type}, {self.color} in color")


mycar = cars("BMW", "2021", "320i", "red")
mycar.cars()
mycar = cars("MERCEDES", "2023", "AMG-gt63s", "black")
mycar.cars()
mycar = cars("VOWLKSWAGEN", "2018", "polo gti", "red")
mycar.cars()
mycar = cars("VOLVO", "2019", "XC90", "aqua")
mycar.cars()
mycar = cars("AUDI", "2022", "TFSI", "luminous")
mycar.cars()

