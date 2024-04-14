from pizzaTopingUsingDecorator.base_pizza import BasePizza
from pizzaTopingUsingDecorator.pizza_decorator import add_toppings


class PizzaCustomize(BasePizza):

   # @add_toppings("c")
    def make_pizza(self):
        return super().make_pizza()
