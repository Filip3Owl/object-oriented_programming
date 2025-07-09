from demoClass import DemoClass

obj = DemoClass()

#  When you call the instance method, Python replaces the self argument with the instance object, obj.
print(f'Calling the instance method result: {obj.instance_method()}')
# output: ('Instance method called', <demoClass.DemoClass object at 0x000001FAEE316900>)

print(f'Calling the class method instead: {obj.class_method()}')
# output: ('Class method called', <class 'demoClass.DemoClass'>)

print(f'Calling the static method: {obj.static_method()}')
# ('Static method called',)