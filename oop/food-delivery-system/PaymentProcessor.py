from abc import ABC, abstractmethod

from Order import Order


class PaymentStrategy(ABC):

    @abstractmethod
    def processPayment(self, amount) -> bool:
        pass


class CreditCardStrategy(PaymentStrategy):
    def processPayment(self, amount):
        return True


class PayPalStrategy(PaymentStrategy):
    def processPayment(self, amount):
        return True


class PaymentProcessor():

    def __init__(self):
        self.paymentStrategy: PaymentStrategy = None

    def SetPaymentStrategy(self, strategyType: str):
        if strategyType == "paypal":
            self.paymentStrategy = PayPalStrategy()
        else:
            self.paymentStrategy = CreditCardStrategy()

    def ProcessPayment(self, order: Order) -> bool:
        if self.paymentStrategy is None:
            raise Exception("Set a payment method first")

        amount = order.GetPrice()
        result = self.paymentStrategy.processPayment(amount)
        return result
