# lib/helpers.py
from models.todo import Todo
from models.user import User

def additional_options():
    from cli import (
        user_menu,
        menu
        )
    while True:
        user_menu()
        choice = input('> ')
        if choice == '0':
            searching_all_user_todo()
        elif choice == '1':
            update_todo()
        elif choice == '2':
            delete_todo()
        elif choice == '3':
            create_todo()
        elif choice == '4':
            complete_Task()
        elif choice == '5':
            menu()
            break
        else:
            print('Invalid Choice')


def search_user():
    additional_options()

def exit_program():
    print("Goodbye!")
    exit()


def searching_all_user_todo():
    user_id = input('Enter user id : ')
    user = User.find_by_id(user_id)

    if user:
        print("User found!!!")
        print("Welcome back")
        todos = Todo.find_by_user_id(user_id)
        if todos:
            for todo in todos:
                print(todo)
    else:
        print('User not found!!!')


def update_todo():
    todo_id = input('Enter Todo id : ')
    todo = Todo.find_by_id(todo_id)

    if todo:
        new_todo = input('Change the todo item: ')
        new_user_id = input('Change User_id: ')
        if new_user_id:
            todo.user_id = int(new_user_id)
        else:
            print('User Id remains Unchanged')
        if type(new_todo) is str and len(new_todo):
            todo.todo = new_todo
            todo.update()
            print('Item Changed')
        else:
            print('Invalid input')
    else:
        print('Todo not found')


def delete_todo():
    todo_id = input('Enter Todo id: ')
    todo = Todo.find_by_id(todo_id)

    if todo:
        todo.delete()
        print('Task Deleted!!!')
    else:
        print('Task Not found!!!')
   

def create_todo():
    user_id = int(input('Enter User id: '))
    todo = input('Enter Todo item: ')

    todo = Todo.create(todo = todo, user_id = user_id)
    print('New Task Created!!!!!!')
    print(todo)

def complete_Task():
    todo_id = int(input('Enter Todo id: '))
    todo =  Todo.completed_todo(todo_id)

    if todo:
        print('Task completed!!!!')
        print(todo)
    else:
        print('Task Not found!!!!')
        
    delete_Task = input('Would you like to Delete the completed Task. Enter Yes or No. ')

    if delete_Task == 'Yes' or 'yes':           
        todo.delete()
        print('Task Deleted')
    else:
        print('Task not deleted')

    return todo 


def list_all_users():
    users = User.get_all()

    for user in users:
        print(f"Name: <({user.name})>")


def list_all_app_todos():
    todos = Todo.get_all_todo()

    for todo in todos:
        print(f"Todo: {todo.todo} | User: {todo.user_id} | Status: {todo.status}")
    



