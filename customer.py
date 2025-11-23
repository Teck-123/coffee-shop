from order import Order

class Customer:
    all = []

    def __init__(self, name="string"):
        self.name = name
        self._orders = []
        Customer.all.append(self)
        
    @property
    def name(self):
        return self._name
    
    @name.setter

    def name(self, value):
     if isinstance(value, str) and 1 <= len(value) <= 15:
    self._name = value
    else: 
    raise ValueError("Name must be a string between 1 and 15 characters long.")
        if isinstance(name, str) and 1 <= len(name) <= 50:
            self._name = name
        else:
            raise ValueError("Name must be a string between 1 and 50 characters long.") 

    def create_order(self, coffee, price):
        new_order = Order(self, coffee, price)
        return new_order
    

    def orders(self):
        return [order for order in Order.all if order.customer == self]
    def coffees(self):
        return list({order.coffee for order in self.orders()})
    def total_spent(self):
        return sum(order.price for order in self.orders())
    def num_orders(self):
        return len(self.orders())
    def average_order_price(self):
        orders = self.orders()
        if not orders:
            return 0
        return sum(order.price for order in orders) / len(orders)

    @classmethod
    def most aficionatio(cls, coffee) 
        great_customer = None
        max_spent = 0   

        for customer in cls.all:
            spent = sum(order.price for order in customer.orders() if order.coffee == coffee)
            if spent > max_spent:
                max spent = spent
                great customer = customer

                return great customer if max spent > 0 else None