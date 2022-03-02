# Lab Professor: Ms. Laily Ajellu
# COMP 2152 - Assignment 1
# Otavio Pereira-Barbosa - 101337690

import employee
import item

# Pre Populate the list
employee_list = []
employee1 = employee.Employee(1001, "Otavio Barbosa", "Hourly", 10, 0, 0, 222333)
employee_list.append(employee1)

item_list = []
item1 = item.Item(1, "Python Course", 199)
item_list.append(item1)


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
                    continue
                elif user_choice == 2:
                    create_item(item_list)
                elif user_choice == 3:
                    make_purchase()
                elif user_choice == 4:
                    summary()
                elif user_choice == 5:
                    print("")
                    print("\t\t\tBye Bye")
                    break
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

        item_name = input("Enter Employee Name: ")

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
            break

    return item_list


def make_purchase():
    print("Test")


def summary():
    print("Test")


if __name__ == "__main__":
    for obj in employee_list:
        print(obj)
    for obj in item_list:
        print(obj)
    menu()
