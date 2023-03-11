from functions import get_todos , write_todos
import time

now = time.strftime('%b %d, %Y  %H:%M:%S')
print("it is",now)
while True:
    user_action = input("type add or show or complete or edit or exit : \n")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]

        todos = get_todos('todo.txt')

        todos.append(todo + '\n')

        write_todos('todo.txt',todos)

    elif user_action.startswith("show"):

        todos = get_todos('todo.txt')

        new_item = [item.strip("\n") for item in todos]

        for index , item in enumerate(new_item):
            print(f"{index + 1}-{item}")

    elif user_action.startswith("edit"):

        try:
            x = int(user_action[5:])

            todos = get_todos('todo.txt')

            new_todo = input("enter the new todo: ")
            todos[x-1] = new_todo + "\n"

            write_todos('todo.txt', todos)

            new_item = [item.strip("\n") for item in todos]

            for index, item in enumerate(new_item):
                print(f"{index + 1}-{item}")

        except ValueError:

            print('invalid command : enter the number of item ou wish to edit')

            continue

    elif user_action.startswith("complete"):

        try:
            x1 = int(user_action[9:])

            todos = get_todos('todo.txt')

            todos.pop(x1-1)

            write_todos('todo.txt', todos)

        except IndexError:

            print('out of range')
            continue

    elif user_action.startswith("exit"):

        break

    else:

        print("invalid command ")


print("bye , program work is done")