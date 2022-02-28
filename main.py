# Lab Professor: Ms. Laily Ajellu
# COMP 2152 - Assignment 1
# Otavio Pereira-Barbosa - 101337690

def menu():
    user_choice = 0
    while user_choice != 5:
        try:
            user_choice = int(input("Enter a valid choice to select it:"))
        except UserWarning:
            print("You have not selected a valid menu item")
        else:
            if user_choice == 1:
                create_employee()
            elif user_choice == 2:
                create_item()
            elif user_choice == 3:
                make_purchase()
            elif user_choice == 4:
                summary()
            elif user_choice == 5:
                break
            else:
                print("Please enter a valid option")


if __name__ == "__main__":
    menu()
