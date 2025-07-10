class Pizza:

    def __init__(self, toppings):
        self.toppings = toppings

    # __repr__ provides a string representation for when you need to display an object.
    def __repr__(self):
        return f"Pizza({self.toppings})"
    
    def add_topping(self, topping):
        self.toppings.append(topping)
    
    def remove_topping(self, topping):
        if topping in self.toppings:
            self.toppings.remove(topping)