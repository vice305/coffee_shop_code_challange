class Cutomer:
    
    def __init__(self, name):
        if not isinstance(name, str):
            raise TypeError("name must be a string")
        if not name:
            raise ValueError("name cannot be empty")
        self.name = name
        Coffee.all_coffees.append(self)

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("name must be a string")
        if not value:
            raise ValueError("name cannot be empty")
        self.__name = value

    def orders(self):
        return [order for order in Order.all_orders if order.customer == self]
    
    def coffees(self):
        return list(set(coffee for order in self.orders() for coffee in order.coffees))
    
    def  create_order(self, coffees, price):
        return Order(self, coffees, price)
    
    @classmethod
    def all_customers(cls,coffees):
        if not isinstance(coffees, Coffee):
            raise TypeError("coffees must be a Coffee instance")
        customer_spending = {}
        for order in coffee.orders():
            if order.customer in customer_spending:
                customer_spending[order.customer] += order.price
            else:
                customer_spending[order.customer] = order.price
            if not customer_spending:
                return None
        return max(customer_spending, key=customer_spending.get)

