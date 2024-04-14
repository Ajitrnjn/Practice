class Vehicle:

    def __init__(self, milage, model):
        self.milage = milage
        self.model = model

    def display(self):
        print("Inside vehicle class")
        print(f"Milage: {self.milage}, Model: {self.model}")
