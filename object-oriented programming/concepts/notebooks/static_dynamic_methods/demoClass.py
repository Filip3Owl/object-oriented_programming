class DemoClass:
    
    def instance_method(self):
        return ("Instance method called", self)
    
    @classmethod
    def class_method(cls):
        return ("Class method called", cls)
    
    @staticmethod
    def static_method():
        return ("Static method called",)