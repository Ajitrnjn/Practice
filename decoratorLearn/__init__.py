from decoratorLearn.decorator import Decorator
from decoratorLearn.pythagoras import Pythagoras

if __name__ == "__main__":
    x = int(input("Enter the 1'st number :"))
    y = int(input("Enter the 2'nd number :"))
    z = int(input("Enter the 3'rd number :"))
    decorator = Decorator(x,y,z)
    val = decorator.square_number()
    is_following = Pythagoras.follow_pythagoras(val)
    print(is_following)
