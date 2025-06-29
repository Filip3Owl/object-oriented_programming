class Sigma:
    def action(self):
        print("Sigma action")

alfa = Sigma() # Create an instance of Sigma
type(alfa)  # <class '__main__.Sigma'>

alfa.action()  # Sigma action

### constructor method

class Red:
    def  __init__(self, color):
        self.color = color # This is an instance variable

class Computer:
    def __init__(self, brand, model, price): # Constructor method
        self.brand = brand
        self.model = model
        self.price = price

factor = Computer("Factor", "X1", 5000)

print(factor.brand)  # Factor
print(factor.model)  # X1
print(factor.price)  # 5000