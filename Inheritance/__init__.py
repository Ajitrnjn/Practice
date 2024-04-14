from Inheritance.Car import Car
from Inheritance.SedanCar import SedanCar
from Inheritance.Vehicle import Vehicle

if __name__ == "__main__":
    car = Car(10, "Camry", 20 )
    car1 = Vehicle(12, "GTO")
    car2 = SedanCar(19,"sedan",25, 6)
    car.display()
    car1.display()
    car2.display()
