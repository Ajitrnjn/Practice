class Decorator:

    def __init__(self, num1, num2, num3):
        self.a = num1
        self.b = num2
        self.c = num3

    def decorator(func):
        def wrapper(*args, **kwargs):
            print("Before function")
            func(*args, **kwargs)
            val = func(*args, **kwargs)
            print("After funtion")
            return val

        return wrapper

    @decorator
    def square_number(self):
        return [self.a * self.a, self.b * self.b, self.c * self.c]
