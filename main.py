# Lab Professor: Ms. Laily Ajellu
# COMP 2152 - Assignment 1
# Otavio Pereira-Barbosa - 101337690

import employee

# Pre Populate the list
employee_list = []
employee1 = employee.Employee(1001, "Otavio Barbosa", "Hourly", 10, 0, 0, 222333)
employee_list.append(employee1)


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
                    create_item()
                elif user_choice == 3:
                    make_purchase()
                elif user_choice == 4:
                    summary()
                elif user_choice == 5:
                    print("")
                    print("\t\t\tBye Bye")
                    menu_active = False
                    break
                else:
                    print("Please enter a valid option")


def create_employee(employee_list):
    employee_id = 0
    employee_years_worked = 0
    print("")
    print(35 * "-")
    print("\t\t\tEmployee Menu")
    print(35 * "-")
    print("")
    while True:
        try:
            employee_id = int(input("Enter an Employee ID: "))
        except ValueError:
            print("You have not entered a number")
            continue
        else:
            for obj in employee_list:
                if employee_id == obj.employee_id:
                    print(f"\nWARNING -Employee ID {employee_id} already exists!"
                          f"\nEmployee ID: {obj.employee_id}, Employee Name: {obj.employee_name}")
                    print("for loop")
                    break
                else:
                    continue
            else:
                break

    employee_name = input("Enter Employee Name: ")
    print(employee_id, employee_name)
    return employee_list

    # while True:
    #     employee_type = input("Enter Employee Type(manager or hourly): ")
    #     if employee_type == "manager" or employee_type == "hourly":
    #         break
    #     else:
    #         continue
    # while True:
    #     try:
    #         employee_years_worked = int(input("Enter Employee Worked Years: "))
    #         break
    #     except ValueError:
    #         print("You have not entered a number")
    #         continue
    # print(employee_id, employee_name, employee_type, employee_years_worked)
    # return employee_list


def create_item():
    print("Test")


def make_purchase():
    print("Test")


def summary():
    print("Test")


if __name__ == "__main__":
    menu()
