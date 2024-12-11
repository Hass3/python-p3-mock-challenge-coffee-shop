class Coffee:

    all = []

    def __init__(self, name):
        if not isinstance(name, str) or len(name) < 3:
            raise ValueError("name must be a string or greater than or equal to 3") 
        self._name = name
        Coffee.all.append(self)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self,name):
        if hasattr(self,"._name"):
            raise AttributeError("name cannot be changed")
        
    def orders(self):
        return [order for order in Order.all if order.coffee == self]
    def customers(self):
        return list(set([order.customer for order in self.orders() if isinstance(order.customer,Customer)]))
        
    def num_orders(self):
        return len(self.orders())
        
    def average_price(self):
        if self.num_orders() == 0:
            return 0
        total_price = sum(order.price for order in self.orders())
        return total_price / self.num_orders()

class Customer:
    all = []
    def __init__(self, name):
        self.name = name
        Customer.all.append(self)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self,name):
        if isinstance(name,str) and  (1<= len(name) <= 15):
            self._name = name

    def orders(self):
        return [order for order in Order.all if order.customer == self]
        
    
    def coffees(self):
        return list(set([order.coffee for order in self.orders() if isinstance(order.coffee,Coffee)]))
        
    def create_order(self, coffee, price):
        new_order =  Order(self,coffee, price)
        return new_order
   
       
class Order:
    all = []
    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        if not isinstance(price,float) or not( 1.0 <= price <= 10.0):
            raise ValueError("Must be a type of float or be between 1.0 and 10.0")        
        self._price = price
        Order.all.append(self)
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self,price):
        if hasattr(self,"._price"):
            raise AttributeError("Price cannot be changed")
    
    @property
    def customer(self):
        return self._customer
    
    @customer.setter
    def customer(self,customer):
        if not isinstance(customer, Customer):
            raise Exception("The Customer must be of the Customer Class")
        self._customer = customer
    
    @property
    def coffee(self):
        return self._coffee
    
    @coffee.setter
    def coffee(self,coffee):
        if not isinstance(coffee, Coffee):
            raise Exception("The coffee must be of the Coffee Class")
        self._coffee = coffee