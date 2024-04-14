from pizzaTopingUsingDecorator.base_pizza import BasePizza
from pizzaTopingUsingDecorator.pizza_customize import PizzaCustomize

if __name__ == "__main__":
    basepizza = BasePizza()
    basepizza.make_pizza()
    customizePizza = PizzaCustomize()
    customizePizza.make_pizza()




