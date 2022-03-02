# Lab Professor: Ms. Laily Ajellu
# COMP 2152 - Assignment 1
# Otavio Pereira-Barbosa - 101337690

class Employee:

    def __init__(self, employee_id, employee_name, employee_type, employee_years, employee_purchased,
                 employee_discounts, employee_discount_number):
        self.employee_id = int(employee_id)
        self.employee_name = employee_name
        self.employee_type = employee_type
        self.employee_years = int(employee_years)
        self.employee_discount_number = int(employee_discount_number)
        self.employee_discounts = employee_discounts
        self.employee_purchased = employee_purchased

    def set_employee_id(self, employee_id):
        self.employee_id = employee_id

    def set_employee_name(self, employee_name):
        self.employee_name = employee_name

    def set_employee_type(self, employee_type):
        self.employee_type = employee_type

    def set_employee_years(self, employee_years):
        self.employee_years = employee_years

    def set_employee_purchased(self, employee_purchased):
        self.employee_purchased = employee_purchased

    def set_employee_discounts(self, employee_discounts):
        self.employee_discounts = employee_discounts

    def set_employee_discount_number(self, employee_discount_number):
        self.employee_discount_number = employee_discount_number

    def get_employee_id(self):
        return self.employee_id

    def get_employee_name(self):
        return self.employee_name

    def get_employee_type(self):
        return self.employee_type

    def get_employee_years(self):
        return self.employee_years

    def get_employee_purchased(self):
        return self.employee_purchased

    def set_employee_discounts(self):
        return self.employee_discounts

    def get_employee_discount_number(self):
        return self.employee_discount_number

    def __str__(self) -> str:
        return f"\nEmployee ID: {self.employee_id}\n" \
               f"Employee Name: {self.employee_name}\n" \
               f"Employee Type: {self.employee_type}\n" \
               f"Employee Years Worked: {self.employee_years}\n" \
               f"Employee Total Purchases: {self.employee_purchased}\n" \
               f"Employee Total Discounts: {self.employee_discounts}\n" \
               f"Employee Discount Number: {self.employee_discount_number}\n"
