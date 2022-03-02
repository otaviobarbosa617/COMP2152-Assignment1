# Lab Professor: M. Laily Ajellu
# COMP 2152 - Assignment 1
# Otavio Pereira-Barbosa - 101337690

class Item:

    def __init__(self, item_number, item_name, item_cost):
        self.item_number = int(item_number)
        self.item_name = item_name
        self.item_cost = int(item_cost)

    def set_item_number(self, item_number):
        self.item_number = int(item_number)

    def set_item_name(self, item_name):
        self.item_name = item_name

    def set_item_cost(self, item_cost):
        self.item_cost = int(item_cost)

    def get_item_number(self):
        return self.item_number

    def get_item_name(self):
        return self.item_name

    def get_item_cost(self):
        return self.item_cost

    def __str__(self) -> str:
        return f"\nItem Number: {self.item_number}\n" \
               f"Item Name: {self.item_name}\n" \
               f"Item Cost: {self.item_cost}\n"
