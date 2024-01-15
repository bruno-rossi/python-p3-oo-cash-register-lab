#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount=0):
    self.discount = discount
    self.total = 0
    self.items = []

  def add_item(self, item, price, quantity=1):
    self.total = self.total + (quantity * price)

    self.last_transaction = quantity * price
    
    for i in range(quantity):
      self.items.append(item)
      i += 1

    return self.items

  def apply_discount(self):
    if self.discount != 0:
      self.total = self.total - (self.total * (float(self.discount) / 100))
      print(f"After the discount, the total comes to ${int(self.total)}.")
    else:
      print("There is no discount to apply.")

  def void_last_transaction(self):
    self.total = self.total - self.last_transaction

if __name__ == '__main__':
  cash_register = CashRegister(20)
  # cash_register.add_item("macbook air", 1000, 2)
  cash_register.add_item("eggs", 1.99, 2)
  cash_register.add_item("tomato", 1.76, 3)
  cash_register.apply_discount()
  # print(float(cash_register.discount))
  print(cash_register.total)