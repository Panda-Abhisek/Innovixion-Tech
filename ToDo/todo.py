class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        self.tasks.remove(task)

    def get_tasks(self):
        return self.tasks

# Example usage
todo_list = TodoList()

print("Enter tasks (press 'q' to quit):")
while True:
    task = input()
    if task == 'q':
        break
    todo_list.add_task(task)

print("\nHere is your Tasks:")
for task in todo_list.get_tasks():
    print(task)
