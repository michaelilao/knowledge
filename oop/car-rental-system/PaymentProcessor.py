from abc import ABC, abstractmethod


class PaymentProcessor(ABC):

    @abstractmethod
    def processPayment(self, amount) -> bool:
        pass


class StripePaymentProcessor(PaymentProcessor):
    def processPayment(self, amount):
        return True
