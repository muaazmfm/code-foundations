from abc import ABC, abstractmethod

# bad
class PaymentProcessorBad:
    def __init__(self, method):
        self.method = method

    def process_payment(self, amount):
        if self.method == "card":
            print("Card payment")
        elif self.method == "cash":
            print("Cash payment")
        elif self.method == "paypal":
            print("PayPal payment")

# good
class PaymentProcessorGood(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

class CardPayment(PaymentProcessorGood):
    def process_payment(self, amount):
        print("Card payment")

class CashPayment(PaymentProcessorGood):
    def process_payment(self, amount):
        print("Cash payment")

class PayPalPayment(PaymentProcessorGood):
    def process_payment(self, amount):
        print("PayPal payment")