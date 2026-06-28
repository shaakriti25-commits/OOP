class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    def display_into(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Year:", self.year)
c1=Car("Lamborghini", "Aventador", 2022)
c1.display_into()
