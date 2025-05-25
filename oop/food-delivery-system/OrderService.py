from typing import List

from User import User, Customer, RestaurantAdmin, DeliveryAgent
from Restaurant import Restaurant
from Order import Order, OrderStatus
from PaymentProcessor import PaymentProcessor
from NotificationService import NotificationService, SMSChannel, EmailChannel


class OrderService():
    def __init__(self):
        self.orders: List[Order] = []
        self.notificationService = NotificationService()
        self.notificationService.AddChannel(EmailChannel())
        self.notificationService.AddChannel(SMSChannel())

        self.paymentProcessor = PaymentProcessor()

    def GetRestaurantOrders(self, restaurant: Restaurant):
        restaurantOrders = []
        for order in self.orders:
            if order.restaurant is restaurant and order.status != OrderStatus.DELIVERED:
                restaurantOrders.append(order)
        print(restaurant.__repr__() + " has " +
              str(len(restaurantOrders)) + " current orders")
        print(restaurantOrders)

        return restaurantOrders

    def GetOpenOrders(self):
        # Return orders that can be picked up for delivery by an agent
        openOrders = []
        for order in self.orders:
            if order.deliveryAgent is None:
                openOrders.append(order)

        print("There are currently " + str(len(openOrders)) +
              " open orders to be assigned to")
        print(openOrders)
        return openOrders

    def AddDeliveryAgentToOrder(self, order: Order, deliveryAgent: DeliveryAgent):
        if order.deliveryAgent is not None:
            raise Exception("Order already has a delivery driver")

        order.deliveryAgent = deliveryAgent

    def StartOrder(self, restaurant: Restaurant, customer: Customer):
        # Create empty order
        newOrder = Order(restaurant, customer)
        print(customer.__str__() + " is starting an order @ " + restaurant.__str__())
        return newOrder

    def FinalizeOrder(self, order: Order, paymentType: str):
        # Get Price from Order

        # Process Payment
        self.paymentProcessor.SetPaymentStrategy(paymentType)
        self.paymentProcessor.ProcessPayment(order)

        # Add order to open orders
        self.orders.append(order)

        # Progress Order
        print("Paying for " + order.__repr__() + " with " +
              paymentType + " for $" + str(order.GetPrice()))

        self.ProgressOrder(order, order.customer, OrderStatus.ORDERED)

    def ProgressOrder(self, order: Order, triggeredByUser: User, nextStep: OrderStatus):
        # Strategy Pattern to ensure correct useres are able to progress order for specifc steps
        # and notifcations are sent when needed

        # set status to next
        message = triggeredByUser.__repr__() + " progresses to step " + nextStep.name
        order.SetStatus(nextStep)

        # notify users
        self.notificationService.Notify(order.customer, message)
        print("")
        self.notificationService.Notify(order.deliveryAgent, message)
        print("")
        self.notificationService.Notify(order.restaurant, message)
        print("")
