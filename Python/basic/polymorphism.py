# simple example of polymorphism

class Shape:
    def area(self):
        print("Calculating area of shape")

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius
    
shapes = [Rectangle(5, 10), Circle(7)]
for shape in shapes:
    print(f"Area: {shape.area()}")


#polymorphism in real-life (Payments) without pass with proper deposit, withraw (add, subtract) methods

class Payment:
    def process_payment(self, amount):
        self.amount = amount

class CreditCardPayment(Payment):
    def process_payment(self, amount):
        super().process_payment(amount)
        print("\n---------------------- Processing Payments Example -----------------\n")
        print(f"Processing credit card payment of ${self.amount}")

class PayPalPayment(Payment):
    def process_payment(self, amount):
        super().process_payment(amount)
        print(f"Processing PayPal payment of ${self.amount}")

class UPIpayment(Payment):
    def process_payment(self, amount):
        super().process_payment(amount)
        print(f"Processing UPI payment of ${self.amount}")

payments = [CreditCardPayment(), PayPalPayment(), UPIpayment()]
for payment in payments:
    payment.process_payment(100)
