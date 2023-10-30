# Development of an e-commerce system

class Products:
    def __init__(self, barcode):
        self.barcode = barcode

class book(Products):
    def __init__(self, barcode, title, author):
        super().__init__(barcode)
        self.title = title
        self.author = author

class clothes(Products):
    def __init__(self, barcode, size, color):
        super().__init__(barcode)
        self.size = size
        self.color = color

class electronics(Products):
    def __init__(self, barcode, brand, model):
        super().__init__(barcode)
        self.brand = brand
        self.model = model
        
class inventory:
    def __init__(self):
        self.products = []

    def add_products(self, products):
        self.products.append(products)

    def remove_products(self, products):
        self.products.remove(products)

