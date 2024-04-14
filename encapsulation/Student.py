class Student:

    def __init__(self, name, roll):
        self._name = name
        self.roll = roll

    def display(self):
        print(f"Name: {self._name}, Roll: {self.roll}")
