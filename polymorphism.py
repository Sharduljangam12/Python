class Payment:
    def pay(self, amount):
        raise NotImplementedError

class CreditCard(Payment):
    def pay(self, amount):
        print(f"Paid ₹{amount} using Credit Card")

class UPI(Payment):
    def pay(self, amount):
        print(f"Paid ₹{amount} using UPI")

class Cash(Payment):
    def pay(self, amount):
        print(f"Paid ₹{amount} using Cash")

def process_payment(payment_method):
    payment_method.pay(500)

# Use cases
process_payment(CreditCard())  # Paid ₹500 using Credit Card
process_payment(UPI())         # Paid ₹500 using UPI
process_payment(Cash())  