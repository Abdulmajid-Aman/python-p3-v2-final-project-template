#!/usr/bin/env python3

from helpers import (
    exit_program,
    search_user,
    list_all_users,
    list_all_app_todos
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            search_user()
        elif choice == '2':
            list_all_users()
        elif choice == '3':
            list_all_app_todos()
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. User Information")
    print("2. List all App Users")
    print("3. List all Todos")    

def user_menu():
    print("Please select an option:")
    print("0. Search for all User Todo")
    print("1. Update Todo") 
    print("2. Delete Todo")  
    print("3. Create a new Todo")
    print("4. Complete a Todo")  
    print("5. Go back")   


if __name__ == "__main__":
    main()
