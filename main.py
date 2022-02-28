# Lab Professor: Ms. Laily Ajellu
# COMP 2152 - Assignment 1
# Otavio Pereira-Barbosa - 101337690

import employee

employee_list = []


def menu():
    menu_active = True
    while menu_active:
        print(35 * "-")
        print("|\t\t\tMain Menu", "|".rjust(13))
        print("| 1 - Create Employee", "|".rjust(13))
        print("| 2 - Create Item", "|".rjust(17))
        print("| 3 - Make Purchase", "|".rjust(15))
        print("| 4 - All Employee Summary", "|".rjust(8))
        print("| 5 - Exit", "|".rjust(24))
        print(35 * "-")
        try:
            user_choice = int(input("Enter a valid choice to select it: "))
        except UserWarning:
            print("You have not selected a valid menu item")
        else:
            if user_choice == 1:
                create_employee(employee_list)
                continue
            elif user_choice == 2:
                create_item()
            elif user_choice == 3:
                make_purchase()
            elif user_choice == 4:
                summary()
            elif user_choice == 5:
                print("")
                print("\t\t\tBye Bye")
                menu_active = False
            else:
                print("Please enter a valid option")


def create_employee(employee_list):
    employee1 = employee.Employee(1001, "Otavio Barbosa", "Hourly", 10, 0, 0, 222333)
    employee_list.append(employee1)
    for obj in employee_list:
        print(obj)
    return employee_list

def create_item():
    print("Test")


def make_purchase():
    print("Test")


def summary():
    print("Test")


if __name__ == "__main__":
    menu()
