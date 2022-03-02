# Lab Professor: Ms. Laily Ajellu
# COMP 2152 - Assignment 1
# Otavio Pereira-Barbosa - 101337690

import employee
import item

# Pre Populate the list
employee_list = []
employee1 = employee.Employee(1001, "John Alber", "hourly", 8, 0, 0, 22737)
employee2 = employee.Employee(1002, "Sarah Rose", "manager", 12, 0, 0, 22344)
employee3 = employee.Employee(1003, "Alex Folen", "manager", 5, 0, 0, 22957)
employee4 = employee.Employee(1004, "Pola Sahari", "hourly", 17, 0, 0, 22488)
employee_list.append(employee1)
employee_list.append(employee2)
employee_list.append(employee3)
employee_list.append(employee4)

item_list = []
item1 = item.Item(11526, "Nike shoes", 120)
item2 = item.Item(11849, "Trampoline", 180)
item3 = item.Item(11966, "Mercury Bicycle", 150)
item4 = item.Item(11334, "Necklace Set", 80)
item_list.append(item1)
item_list.append(item2)
item_list.append(item3)

purchase_list = []

def menu():
    while True:
        print(35 * "-")
        print("|\t\t\tMain Menu", "|".rjust(13))
        print("| 1 - Create Employee", "|".rjust(13))
        print("| 2 - Create Item", "|".rjust(17))
        print("| 3 - Make Purchase", "|".rjust(15))
        print("| 4 - All Employee Summary", "|".rjust(8))
        print("| 5 - Exit", "|".rjust(24))
        print(35 * "-")
        while True:
            try:
                user_choice = int(input("Enter a valid choice to select it: "))
            except ValueError:
                print("You have not selected a valid menu item")
                continue
            else:
                if user_choice == 1:
                    create_employee(employee_list)
                    break
                elif user_choice == 2:
                    create_item(item_list)
                    break
                elif user_choice == 3:
                    make_purchase(item_list, employee_list, purchase_list)
                    break
                elif user_choice == 4:
                    summary()
                elif user_choice == 5:
                    print("")
                    print("\t\t\tBye Bye")
                    exit()
                else:
                    print("Please enter a valid option")


def create_employee(employee_list):
    employee_id = 0
    employee_years_worked = 0
    employee_purchased = 0
    employee_discounts = 0
    employee_discount_number = 0
    print("")
    print(35 * "-")
    print("\t\t\tEmployee Menu")
    print(35 * "-")
    print("")
    while True:
        while True:
            try:
                employee_id = int(input("Enter an Employee ID: "))
            except ValueError:
                print("You have not entered a number")
                continue
            else:
                for obj in employee_list:
                    if employee_id == obj.employee_id:
                        print(f"\nWARNING - Employee ID {employee_id} already exists!"
                              f"\nEmployee ID: {obj.employee_id}, Employee Name: {obj.employee_name}")
                        print("Please, try again!")
                        print("")
                        break
                    else:
                        continue
                else:
                    break

        employee_name = input("Enter Employee Name: ")

        while True:
            employee_type = input("Enter Employee Type (manager or hourly): ").lower()
            if employee_type == "manager" or employee_type == "hourly":
                break
            else:
                print("")
                print("You have not entered the correct Employee Type")
                print("Please, try again!")
                print("")
                continue

        while True:
            try:
                employee_years_worked = int(input("Enter Employee Worked Years: "))
                break
            except ValueError:
                print("")
                print("You have not entered a number of worked years")
                print("Please, try again!")
                print("")
                continue

        while True:
            try:
                employee_discount_number = int(input("Enter Employee Discount Number: "))
            except ValueError:
                print("")
                print("You have not entered a number for Employee Discount")
                print("Please, try again!")
                print("")
                continue
            else:
                for obj in employee_list:
                    if employee_discount_number == obj.employee_discount_number:
                        print(f"\nWARNING - Employee Discount Number {employee_discount_number} already exists!"
                              f"\nEmployee ID: {obj.employee_id}, Employee Name: {obj.employee_name}, Employee Discount"
                              f" Number: {obj.employee_discount_number}")
                        print("Please, try again!")
                        print("")
                        break
                    else:
                        continue
                else:
                    break

        new_employee = employee.Employee(employee_id, employee_name, employee_type, employee_years_worked,
                                         employee_discounts, employee_purchased, employee_discount_number)
        employee_list.append(new_employee)
        print("Your new employee:")
        print(new_employee)
        print(f"Employee {employee_name} added with success")
        print("")

        employee_menu_choice = input("Do you wish to add more employees? "
                                     "Press enter to continue or Type NO to stop: ").lower()
        if employee_menu_choice != "no":
            continue
        else:
            print("")
            print("Back to Main Menu")
            menu()
            break

    return employee_list


def create_item(item_list):
    item_number = 0
    item_cost = 0
    print("")
    print(35 * "-")
    print("\t\t\tItem Menu")
    print(35 * "-")
    print("")
    while True:
        while True:
            try:
                item_number = int(input("Enter an Item Number: "))
            except ValueError:
                print("You have not entered a number")
                continue
            else:
                for obj in item_list:
                    if item_number == obj.item_number:
                        print(f"\nWARNING - Item Number {item_number} already exists!"
                              f"\nItem Number: {obj.item_number}, Item Name: {obj.item_name}")
                        print("Please, try again!")
                        print("")
                        break
                    else:
                        continue
                else:
                    break

        item_name = input("Enter Item Name: ")

        while True:
            try:
                item_cost = int(input("Enter Item Cost: "))
                break
            except ValueError:
                print("")
                print("You have not entered a number for Item Cost")
                print("Please, try again!")
                print("")
                continue

        new_item = item.Item(item_number, item_name, item_cost)
        item_list.append(new_item)
        print("Your new item:")
        print(new_item)
        print(f"Item {item_name} added with success")
        print("")

        item_menu_choice = input("Do you wish to add more items? "
                                 "Press enter to continue or Type NO to stop: ").lower()
        if item_menu_choice != "no":
            continue
        else:
            print("")
            print("Back to Main Menu")
            menu()
            break

    return item_list


def print_items_list(item_list):
    print("")
    print("Item List:")
    print("")
    print(f'{"Item Number |":2} {"Item Name":14} {"| Item Cost":13}')
    for obj in item_list:
        print(f'{obj.item_number:<11} | {obj.item_name:15}| ${obj.item_cost:<9}')
    print("")
    return


def find_employee(employee_list):
    global employee_selected
    while True:
        print("22737 for test")
        try:
            employee_discount_number = int(input("Enter an Employee Discount Number: "))
        except ValueError:
            print("You have not entered a number")
            continue
        else:
            for obj in employee_list:
                if employee_discount_number == obj.employee_discount_number:
                    print(f"{employee_discount_number} found! Employee Name: {obj.employee_name}")
                    print("")
                    employee_selected = obj
                    break
                else:
                    continue
            else:
                print(f"{employee_discount_number} not found on the Employee List")
                print("")
                continue
            break
    return employee_selected


def purchase_item(item_list):
    global item_selected
    while True:
        try:
            item_number = int(input("Enter an Item Number: "))
        except ValueError:
            print("You have not entered a number")
            continue
        else:
            for obj in item_list:
                if item_number == obj.item_number:
                    print(f"{item_number} found! Item Name: {obj.item_name}")
                    print("")
                    item_selected = obj
                    break
                else:
                    continue
            else:
                print(f"{item_number} not found on the Item List")
                continue
            break
    return item_selected


def calculate_discount(employee_selected):
    global discount_total
    if employee_selected.get_employee_discounts() < 200:
        discount_total = min((employee_selected.get_employee_years() * 0.02), 0.10)
        discount_type = employee_selected.get_employee_type()
        if discount_type == "manager":
            discount_total += 0.10
            return discount_total
        else:
            discount_total += 0.02
            return discount_total
    else:
        print("Employee doesn't have any discount allowance")
        return discount_total


def confirm_purchase(item_selected, employee_selected, purchase_list):
    while True:
        print("")
        print("Purchase - Details:")
        print(f"Item: {item_selected.item_name}, ${item_selected.item_cost} "
              f"for Employee: {employee_selected.employee_name}, {employee_selected.employee_discount_number}")

        calculate_discount(employee_selected)

        if discount_total != 0:
            print(f"{employee_selected.employee_name} has a total discount of {discount_total * 100:.1f}%")
        else:
            print(f"{employee_selected.employee_name} does not have a discount allowance")

        discount_amount = discount_total * item_selected.item_cost
        final_price_item = item_selected.item_cost - discount_amount
        print(f"Item has the final price of {final_price_item}")

        while True:
            user_confirm_purchase = input("Do you wish to "
                                          "confirm this purchase? Type YES to confirm or NO to Cancel: ").lower()
            if user_confirm_purchase == "yes":
                employee_total_purchases = employee_selected.get_employee_purchased()
                employee_total_purchases += final_price_item
                employee_selected.set_employee_purchased(employee_total_purchases)

                employee_total_discount = employee_selected.get_employee_discounts()
                employee_total_discount += discount_amount
                employee_selected.set_employee_discounts(employee_total_discount)
                purchase_list.append(item.Item(item_selected.item_number, item_selected.item_name, final_price_item))
                break
            else:
                print("Cancel")
                break
        break
    return purchase_list


def make_purchase(item_list, employee_list, purchase_list):
    print("")
    print(35 * "-")
    print("\t\t\tPurchase Menu")
    print(35 * "-")
    while True:
        print_items_list(item_list)
        find_employee(employee_list)
        calculate_discount(employee_selected)
        purchase_item(item_list)
        confirm_purchase(item_selected, employee_selected, purchase_list)
        purchase_menu_choice = input("Do you wish to add more items? "
                                     "Press enter to continue or Type NO to stop: ").lower()
        if purchase_menu_choice != "no":
            continue
        else:
            print(f"{employee_selected.employee_name} has confirmed the following purchases: ")
            total_amount_transaction = 0
            for obj in purchase_list:
                print(obj)
                total_amount_transaction += obj.item_cost
            print(f"Total amount of this purchase: {total_amount_transaction}")
            print("")
            print("Back to Main Menu")
            menu()
            break


def summary():
    print("Test")


if __name__ == "__main__":
    menu()
