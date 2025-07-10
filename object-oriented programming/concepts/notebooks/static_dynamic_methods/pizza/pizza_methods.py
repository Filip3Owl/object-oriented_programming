from pizza import Pizza

a_pizza = Pizza(["Cheese", "Tomatoes"])
print(a_pizza)

a_pizza.add_topping("Garlic")
print(a_pizza)

a_pizza.remove_topping("cheese")
print(a_pizza)

# So, when should you use instance methods? In short, you should use instance methods when you need to access and edit the data that an instance of your class holds.

