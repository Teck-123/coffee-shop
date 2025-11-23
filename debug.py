from customer import Customer
from coffee import Coffee
from order import Order

c1 = Customer("Jane")
c2 = Customer("Audrey")
c3 = Customer("Carol")

latte = Coffee("latte")
cappuccino = coffee("cappuccino")

c1 = c1.create_order(cappuccino, 4.5)
c2 = c2.create_order(latte, 7.1)

print(f"{c1.name} has spent a total of ${c1.spent():.2f} on coffee.")
print(f"{c2.name} has spent a total of ${c2.spent():.2f} on coffee.")

print(f"Average price of{cappiccino.name} orders:${cappucciono.average_price():.2f}")
print(f"Average price of{latte.name} orders:${latte.average_price():.2f}")

print(f"Most aficionado for cappuccino: {Customer.most_aficionado(cappuccino).name}")
print(f"Most aficionado for latte: {Customer.most_aficionado(latte).name}")
print(f"Most aficionado for latte: {Customer.most_aficionado(latte)}")
print(f"Number of orders for {cappuccino.name}: {cappuccino.num_orders()}")
print(f"Number of orders for {latte.name}: {latte.num_orders()}")   
print(f"Number of orders by {c1.name}: {c1.num_orders()}")
print(f"Number of orders by {c2.name}: {c2.num_orders()}")

