from collections import deque

class Todo(object):
    def __init__(self, todoDesc, hasPriority=False):
        self.todoDesc = todoDesc
        self.hasPriority = hasPriority

    def __str__(self):
        prio_text = "High" if self.hasPriority else "Low"
        return "To do first: {0}, Priority: {1} ".format(self.todoDesc, prio_text)
    
todo_queue = deque()

def add_todo (todo):
    if todo.hasPriority:
        todo_queue.appendleft(todo)
    else:
        todo_queue.append(todo)

def first_todo_inline():
    return todo_queue.popleft()

def print_todos():
    for i,t in enumerate(todo_queue, 1):
        print(f"{i}. {t.todoDesc}")

def main():
    print("To Do List:")
    add_todo(Todo("Clean house"))
    add_todo(Todo("Write a letter"))
    add_todo(Todo("Go grocery shopping", True))
    print_todos()
    print(first_todo_inline())
    return

if __name__ == "__main__":
    main()