
from DeliverySystem import DeliverySystem
from Restaurant import Restaurant, RestaurantType
from User import Customer, DeliveryAgent, RestaurantAdmin
from Item import Item
from Order import OrderStatus

ds = DeliverySystem()


cust = Customer("Michael", "michaelilao@live.com", "647-927-3012")
delivery = DeliveryAgent("Jeff", "jeff@uber.com", "416-925-1236")
jimmy = RestaurantAdmin("Jimmy", "jimmy@jimmythegreek.com", "647-233-7421")

jimmyTheGreek = Restaurant(
    "Jimmy the Greek", RestaurantType.GREEK, "123-456-789")

jimmyTheGreek.AddItem(Item("Potatoes", 5))
jimmyTheGreek.AddItem(Item("Lamb", 12))


ds.AddRestaurant(jimmyTheGreek)

openRestuarants = ds.GetOpenRestaurants()
firstOpen = openRestuarants[0]

menu = firstOpen.menu
myOrder = ds.orderService.StartOrder(firstOpen, cust)
myOrder.AddItems(menu.items[0])
myOrder.AddItems(menu.items[1])

ds.orderService.FinalizeOrder(myOrder, "credit")
print("")


jimmyOrders = ds.orderService.GetRestaurantOrders(jimmyTheGreek)
for o in jimmyOrders:
    ds.orderService.ProgressOrder(o, jimmy, OrderStatus.COOKING)

print("")
openOrders = ds.orderService.GetOpenOrders()
for o in openOrders:
    ds.orderService.AddDeliveryAgentToOrder(o, delivery)
    ds.orderService.ProgressOrder(o, delivery, OrderStatus.ENROUTE)
    ds.orderService.ProgressOrder(o, delivery, OrderStatus.DELIVERED)
