#!/usr/bin/env python3
# lib/debug.py

from models.__init__ import CONN, CURSOR
from models.user import User
from models.todo import Todo
import ipdb

User.drop_table()
Todo.drop_table()

User.create_table()
Todo.create_table()

# Create instances of User class

user1 = User.create("John Doe")
user2 = User.create("Jane Doe")
user3 = User.create("Bob Smith")
user4 = User.create("Alice Johnson")
user5 = User.create("Mike Brown")

# Create instances of Todo class
todo1 = Todo.create("Buy milk", 1)
todo2 = Todo.create("Walk the dog", 1)
todo3 = Todo.create("Do laundry", 2)
todo4 = Todo.create("Clean the house", 2)
todo5 = Todo.create("Study for exam", 3)

user2 = User.find_by_id(2)  # assuming user2 has id 2
todo6 = Todo.create("Go to gym", 4)
todo7 = Todo.create("Read a book", 4)
todo8 = Todo.create("Call a friend", 5)
todo9 = Todo.create("Watch a movie", 5)
todo10 = Todo.create("Play video games", 3)


ipdb.set_trace()
