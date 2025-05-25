# Food Delivery System

## Requirements
- Browse restraurants, view menus, place orders
- Restraurants manage their menus, prices, availability
- Delivery Agents should accept/fufill orders
- System should handle order tracking and status update
- System should support multiple payment methods
- System should provide real-time notifications to customer, restaurant and delivery agents



## Assumptions
- Should we allow for user to cancel order? No
- Do we need to handle payment to delivery agents and restaurants? No



## Objects

Restaurant
- Name
- Type
- Menu
- Type (Chineese, Indian, Mexican)
- OperatingHours[]
- SetOperatingHours(day, openTime, closeTime)
- IsOpen()
- AddItem(item)

OperatingHours
- day (Monday, ..., Sunday)
- openTime
- closeTime

Menu
- Items[]

Item
- Name
- Price


Users (Parent Class) -> Customer, Delivery Agent, Restaurant Admin
- Name
- Phone
- Update()

// Observer Pattern


OrderService
- Orders[]
- AcceptOrder(Order)
- GetOpenOrders()
- NotificationService
- StartOrder(customer, restaurant)
- FinalizeOrder(order)
- ProgressOrder(order, triggeredByUser, nextStep) // Updates order status and notfies agents



Order
- Restaurant
- Customer
- Items
- DeliveryAgent
- Status (Pending, Ordered, Cooking, EnRoute, Delivered)
- AddItems(Item)
- SetStatus(Status)


NotificationService
- notify(Order)

DeliverySystem
- Restaurants[]
- OrderSystem
- GetOpenRestaurants()

PaymentProcessor 
- PaymentStrategy
- SetPaymentStrategy
- ProcessPayment(Order)

PaymentStrategy -> Paypal, Credit, Klarna




Sequence Diagram
1. User searches open restaurants
2. User starts an order at a restaurant
3. User adds items to order
4. User finalizes order
5. Restaurant starts cooking order
6. Delivery Agent searches open orders
7. Delivery Agent accepts order
8. Restaurant finishes cooking order.
9. User & Delivery Agent are notified
10. Delivery Agent picks up food
11. User is notified
12. Food is dropped off
13. User is notified