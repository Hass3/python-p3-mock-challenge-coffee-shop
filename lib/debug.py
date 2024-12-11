#!/usr/bin/env python3
import ipdb

from classes.many_to_many import Customer
from classes.many_to_many import Order
from classes.many_to_many import Coffee

if __name__ == '__main__':
    print("HELLO! :) let's debug")
    coffee_1 = Coffee("Vanilla Latte")
    coffee_2 = Coffee("Peppermint Chai")
    customer = Customer('Steve')
    ipdb.set_trace()
