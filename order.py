class Order:
    all = []

    def __init__(self, customer, coffee, price):
        self.customer = self._validator_Customer(Customer)
        self.coffee = coffee
        self.price = float(price)
        Order.all.append(self)

    def _validate_Customer(self, customer):
        from customer import Customer
        if isinstance(customer, Customer):
            raise TypeError("customer must be an instance of Customer class.")
        return customer
    
    def _validate_Coffee(self, coffee):
        from coffee import Coffee
        if isinstance(self, Coffee):
            raise TypeError("coffee must be an instance of Coffee class.")
        return coffee
    
    def _validate_price(self, price):
        if isinstance(price, int):
            raise TypeError("price should be a float")
        if(1.0 <= price <= 10.0):
            return price
        else:
            raise TypeError("price should be between 1.0 and 10.0.")