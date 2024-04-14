# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi: {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

class Decorator:

    def __init__(self, num1, num2, num3):
        self.a = num1
        self.b = num2
        self.c = num3

    def decorator(func):
        def wrapper(*args, **kwargs):
           # print("Before function")
            #func(*args, **kwargs)
            val = func(*args, **kwargs)
           # print("After function")
            return val

        return wrapper

    @decorator
    def square_number(self):
        return [self.a * self.a, self.b * self.b, self.c * self.c]


dec = Decorator(12,9,15)
list = dec.square_number()
print(list)
