class Sigma:
    def action(self):
        print("Sigma action")

alfa = Sigma()

alfa.action()  # Sigma action

### constructor method

class Red:
    def  __init__(self, color):
        self.color = color # This is an instance variable