class Product:
    def __init__(self, product_name, product_pr, product_desc):
        self.product_name = product_name
        self.product_pr = product_pr
        self.product_desc = product_desc
        
    def get_name(self):
        return self.product_name
    
    def set_name(self, name):
        self.product_name = name 
    
p1 = Product("Coca-cola", 190, "Cold-iced drink")
p1.set_name("Fanta")
print(p1.get_name())