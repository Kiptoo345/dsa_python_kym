class Product:
    def __init__(self, product_name, product_price, product_desc):
        self.product_name = product_name
        self.product_price = product_price
        self.product_desc = product_desc
    
    def get_name(self):
        return self.product_name
    
    def set_name(self, name):
        self.product_name = name

p1 = Product("Tablet", 963258, "qwerty")
print(p1.get_name())
    