class Person:
    adm = 'admin'

    def __init__(self, name):
        self.name = name 

        msg = 'Class in execution' #msg object variable is not available outside the __init__ method
        print(msg)

    def method1(self):
        print(f'Hello {self.name}, you are an {self.adm}')
        pass

instance = Person('Anthony Hopkins')
instance.method1()

class Admin:
    def  __init__(self, name, msg):
        self.name = name
        self.msg = msg # msg is an instance variable, available to all methods of the class
        print(f'Admin {self.name} created with message: {self.msg}')

    def method2(self):
        print(f'Admin {self.name} says: {self.msg}')

instance2 = Admin('Anthony Hopkins', 'Welcome to the admin panel')

class test:
    name = 'Clark Kent'

    def __init__(self, name):
        self.name = 'Lex Luthor'

start = test()
print(start.name)
