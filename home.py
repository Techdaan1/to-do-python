from collections import deque

class Todo(object):
    def __init__(self, todoDesc, hasPriority=False):
        self.todoDesc = todoDesc
        self.hasPriority = hasPriority

    def __str__(self):
        prio_text = "High" if self.hasPriority else "Low"
        return "{0}, Priority: {1} ".format(self.todoDesc, prio_text)
    
todo_queue = deque()

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

def main():
  while True:
        print("\nMenu:")
        print("1. Add a to-do")
        print("2. Show all to-dos")
        print("3. Get the first to-do in line")
        print("4. Exit")
        choice = input("Choose an option (1-4): ")
        print()

        if choice == '1':
            desc = input("Enter the to-do description: ")
            prio = input("Is it a high priority? (yes/no): ").strip().lower() == 'yes'
            add_todo(Todo(desc, prio))
        elif choice == '2':
            print("To Do List:")
            print_todos()
        elif choice == '3':
            if todo_queue:
                print("First to-do:", first_todo())
            else:
                print("No to-dos in the list.")
        elif choice == '4':
            print("Leave menu")
            break
        else:
            print("Invalid option, please choose again.")
if __name__ == "__main__":
    main()