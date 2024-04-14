from Inheritance import Car


class SedanCar(Car):

    def __init__(self, milage, model, speed, airbag):
        super().__init__(milage, model, speed)
        self.airbag = airbag

    def display(self):
        super().display()
        print(f"Airbag: {self.airbag}")
