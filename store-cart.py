# Product - name, price, stock
# Customer - name
# CartItems - product, quantity
# Cart - User, CartItems
# Payment - (Paypal, Credit Card)


# 1. Product class
class Product:
    def __init__(self, name, price, stock):
        # Initializing product attributes
        self.name = name
        self.price = price
        self.stock = stock
    
    def __str__(self):
        # String representation of the product
        return f"{self.name}-${self.price}-{self.stock}"

# 2. Customer class
class Customer:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

# 3. CartItems class
class CartItems:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

    def get_total_price(self):
        return self.product.price * self.quantity

# 4. Cart class
class Cart:
    def __init__(self, customer):
        self.customer = customer
        self.cart = []
    
    def add_to_cart(self, product, quantity):
        self.cart.append(CartItems(product, quantity))
    
    def calculate_total(self):
        total_price = 0
        for item in self.cart:
            total_price += item.get_total_price()
        return total_price
    
    def display_cart(self):
        print(f"shopping cart of {self.customer}")
        for item in self.cart:
            print(f"{item.product.name} * {item.quantity} - ${item.get_total_price()}")
        print(f"Total: $ {self.calculate_total()}")

# 5. Tools for defining abstract base classes 
from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod 
    def pay():
        # Abstract method for payment
        pass

class CreditCard(Payment):
    def pay(self, amount):
        # Implementing payment using credit card
        print(f"Paid $ {amount} using credit card")

class Paypal(Payment):
    def pay(self, amount):
        print(f"Paid ${amount} using paypal")

# Creating product instances
laptop = Product('laptop', 10000, 10)
phone = Product('Iphone', 20000, 20)

# Creating customer instance
abdur = Customer('Abdur')

# Creating cart instance for the customer
abdur_cart = Cart(abdur)

# Adding items to the cart
abdur_cart.add_to_cart(laptop, 2)
abdur_cart.add_to_cart(phone, 1)

# Displaying the cart
abdur_cart.display_cart()

# Creating payment instance and making payment
# credit_card = CreditCard()
# credit_card.pay(abdur_cart.calculate_total())

paypal = Paypal()
paypal.pay(abdur_cart.calculate_total())

# Uncomment to print customer and product details
# print(abdur)
# print(laptop)
# print(phone)



#output
"""
shopping cart of Abdur
laptop * 2 - $20000
Iphone * 1 - $20000
Total: $ 40000
Paid $40000 using paypal

"""