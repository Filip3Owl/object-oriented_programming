from pizza import Pizza

a_pizza = Pizza(["Cheese", "Tomatoes"])


a_pizza.add_topping("Garlic")


a_pizza.remove_topping("cheese")


# So, when should you use instance methods? In short, you should use instance methods when you need to access and edit the data that an instance of your class holds.

#When to use class methods

#Some pizza variations

Pizza(['mozzarella', 'tomatoes'])
Pizza(['mozzarella', 'tomatoes', 'ham', 'mushrooms'])
Pizza(['mozzarella'])

# factory methods

class Pizza:

    def __init__(self, toppings):
        self.toppings = list(toppings)

    # __repr__ provides a string representation for when you need to display an object.
    def __repr__(self):
        return f"Pizza({self.toppings})"
    
    def add_topping(self, topping):
        self.toppings.append(topping)
    
    def remove_topping(self, topping):
        if topping in self.toppings:
            self.toppings.remove(topping)
    
    @classmethod
    def margherita(cls):
        return cls(["mozzarella", "tomatoes"])
    
    #don't repeat yourself (dry)
    @classmethod
    def prosciutto(cls):
        return cls(["mozzarella", "tomatoes", "ham"])
