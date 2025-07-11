from pizza_methods import Pizza

print(Pizza.prosciutto())
print(Pizza.margherita())

a_pizza = Pizza.margherita()

a_pizza.add_topping("garlic")

print(f'New topping: {a_pizza}')