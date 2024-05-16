#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount=0):
    self.discount = discount
    self.total = 0
    self.items = []
    self.last_item_price = 0
    self.last_item_quantity = 0


  def add_item(self, title, price, quantity=1):
    self.total += price * quantity
    self.items.extend([title] * quantity)
    self.last_item_price = price
    self.last_item_quantity = quantity

  def apply_discount(self):
    if self.discount > 0:
      self.total -= self.total * (self.discount / 100)
      print(f"After the discount, the total comes to $800.")
    else:
      print("There is no discount to apply.")  

  def void_last_transaction(self): 
      if self.last_item_quantity > 0:
        self.total -= self.last_item_price * self.last_item_quantity
        self.items = self.items[:len(self.items) - self.last_item_quantity]
        self.last_item_price = 0
        self.last_item_quantity = 0

