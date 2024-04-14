from pizzaTopingUsingDecorator.base_pizza import BasePizza


def add_toppings(toppings):
    def wrapper():
        pizza = BasePizza()
        val = pizza.make_pizza() + toppings
        return val

    return wrapper




