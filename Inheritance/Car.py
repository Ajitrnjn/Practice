from Vehicle import Vehicle


class Car(Vehicle):

    def __init__(self, milage, model, speed):
        super().__init__(milage, model)
        self.speed = speed

    def display(self):
        print("inside car class")
        super().display()
        print(f"Speed: {self.speed}")
