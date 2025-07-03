class Console():
    def __init__(self, brand, model, price = False, release = False): # Constructor with optional parameters
        self.brand = brand
        self.model = model
        self.price = price
        self.release = release
    

console1 = Console('Sony', 'PlayStation 5', 499.99, '2020-11-12')
console2 = Console('Microsoft', 'Xbox Series X')

# Displaying console information
print(f'Console 1: {console1.brand} {console1.model} - Price: {console1.price} - Release Date: {console1.release}')
print(f'Console 2: {console2.brand} {console2.model} - Price: {console2.price} - Release Date: {console2.release}')