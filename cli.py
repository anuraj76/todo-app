#prompt = 'Enter a Task:'
#todo1 = input(prompt)
#todo2 = input(prompt)
#todo3 = input(prompt)

#todos = [todo1, todo2, todo3, 'Hello']
#print(todos)

#print(type(todo1))

#user_prompt = 'Enter a Todo:'
#todo1 = input(user_prompt)
#odo2 = input(user_prompt)
#todo3 = input(user_prompt)

#todos = [todo1,todo2,todo3]
#print(todos)
#print(type(user_prompt))
#print(type(todos))

#Automate the todo function -- :
# 2nd Day

# user_prompt = "Enter a todo:"
# todos = []
# while True:
#     todo = input(user_prompt)
#     print(todo.capitalize())
#     todos.append(todo)
#     print(todos)


# todos = []
#
# while True:
#     user_action = input("Type add, show or exit: ")
#     user_action = user_action.strip()
#
#     match user_action:
#         case 'add':
#             todo = input("Enter a Todo: ")
#             todos.append(todo)
#         case 'show':
#             for item in todos:
#                 item = item.title()
#                 print(item)
#
#
#         case 'exit':
#             break
#         case _:
#             print("You have entered a random command")
#
# print ('Thanks for using the app')




#Section 4 : Day 3

#Batch Operations with Python

# meals = ['pasta','pizza','goat']
#
# for i in meals:
#     print(i.capitalize())


#Section 5 : Day 4



# Define Functions
# from functions import get_todos, write_todos
import functions

import time

now = time.strftime("%b-%d-%Y %H:%M:%S")
print('It is ', now)

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()


    if user_action.startswith("add") :
        # todo = input("Enter a todo : ")

        todo = user_action[4:]

        todos = functions.get_todos()

        # file = open('Files/todo.txt', 'r')
        #
        # todos = file.readlines()
        # file.close()

        todos.append(todo + '\n')

        functions.write_todos(todos)

        # file = open('Files/todo.txt', 'w')
        # file.writelines(todos)
        # file.close()
    elif user_action.startswith("show"):

        todos = functions.get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            print(f"{index + 1}-{item}")

        # file = open('Files/todo.txt', 'r')
        # todos = file.readlines()
        # file.close()

        # new_todos = [item.strip('\n') for item in todos]

        # for item in todos:
        #     new_item = item.strip('\n')
        #     new_todos.append(new_item)

        # print(todos)


    elif user_action.startswith("edit"):

        try:

            # (number) = int(input("Number od Todo item : "))
            # number  = number - 1

            number = int(user_action[5:])
            number = number -1
            todos = functions.get_todos()
            # print("Here is existing Todos:", todos)
            #number = int(number)
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + '\n'
            functions.write_todos(todos)

        except ValueError:
            print('Your command is not Valid')
            user_action = input("Type add, show, edit, complete or exit: ")
            user_action = user_action.strip()
            continue

        # print('here is how it will be :', todos)

    elif user_action.startswith("complete"):

        try:
            number = int(user_action[9:])
            # number = int(input("Number of the todo to complete: "))
            todos = functions.get_todos()
            index = number-1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            functions.write_todos(todos)

            message = f"Todo {todo_to_remove} was removed from the list"
            print(message)

        except IndexError:
            print('There happens to be no Item with that number')
            continue

    elif user_action.startswith("exit"):
        break
    else: print("Commmand is invalid")


print ('Thanks for using the app')


