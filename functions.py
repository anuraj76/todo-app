def get_todos(filepath='Files/todo.txt'):
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local



def write_todos(todos_arg,filepath='Files/todo.txt'):
    with open(filepath, 'w') as file:
        todos = file.writelines(todos_arg)

if __name__ == "__main__":
    print('Hello from function')
    print(get_todos())


