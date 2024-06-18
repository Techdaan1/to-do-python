from collections import deque

class Todo(object):
    def __init__(self, todoDesc, hasPriority=False):
        self.todoDesc = todoDesc
        self.hasPriority = hasPriority

    def __str__(self):
        prio_text = "High" if self.hasPriority else "Low"
        return "{0}, Priority: {1} ".format(self.todoDesc, prio_text)
    
todo_queue = deque()
removed_todo_queue = deque()

def add_todo (todo):
    if todo.hasPriority:
        todo_queue.appendleft(todo)
    else:
        todo_queue.append(todo)

def first_todo():
    return todo_queue.popleft()

def print_todos():
    if not todo_queue:
        print("There are no to-dos in the list.")
        return
    for i,t in enumerate(todo_queue, 1):
        print(f"{i}. {t}")

def remove_todo():
    if not todo_queue:
        print("There are no to-dos to remove.")
        return
    print("To Do List:")
    print_todos()
    try:
        index = int(input("Enter the number of the to-do to remove: ")) - 1
        if 0 <= index < len(todo_queue):
            removed = todo_queue[index]
            removed_todo_queue.append(removed)
            del todo_queue[index]
            print(f"Removed: {removed}")
        else:
            print("Invalid number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def main():
  while True:
        print("\nMenu:")
        print("1. Add a to-do")
        print("2. Show all to-dos")
        print("3. Get the first to-do in line")
        print("4. Remove to-do" )
        print("5. Exit")
        choice = input("Choose an option (1-5): ")
        print()

        if choice == '1':
            desc = input("Enter the to-do description: ")
            prio = input("Is it a high priority? (yes/no): ").strip().lower() == 'yes'
            add_todo(Todo(desc, prio))
        elif choice == '2':
            print("To Do List:")
            print_todos()
            print()
            print("Removed To Do List:")
            if not removed_todo_queue:
                print("There are no removed to-dos")
            else:
                print_todos(removed_todo_queue)
        elif choice == '3':
            if todo_queue:
                print("First to-do:", first_todo())
            else:
                print("No to-dos in the list.")
        elif choice == '4':
            remove_todo()
        elif choice == '5':
            print("Leave menu")
            break
        else:
            print("Invalid option, please choose again.")
if __name__ == "__main__":
    main()