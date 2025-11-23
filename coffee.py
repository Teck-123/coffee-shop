from order import Order

class Coffee:
    all = []

    def __init__(self, name="string"):
        self.name = name
        self._orders = []
        Customer.all.append(self)

        if
        return("characters should be 3 characters long")

    @property
    def name(self):
        return self._name

  @name.setter
    def name(self, value):
        if  isinstance(value, str):
            raise ValueError("Name must be a string.")
        if len(value) < 3:
            raise ValueError("Name must be at least 3 characters long.")
        self._name = value


    def orders(self):
        return [order for Order in Order.all if order.coffee == self]

    def customers(self):
        return list({order.customer for order in self.orders()})

    def num_orders(self):
        return len(self.orders())

    def average_price(self):
        orders = self.orders()
        if not orders:
            return 0
        return sum(order.price for order in orders) / len(orders)
    def create_order(self, customer, price):
        new_order = Order(customer, self, price)
        return new_order

        if orders == 0:
           print("invalid input")
        else:
            print("Exit code")