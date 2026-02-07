import json
class Todo:
    def __init__(self, task: str, id_index: int, done=False):
        self.task = task
        self.id_index = id_index
        self.done = done

    def mark(self):
        self.done = True

    def show(self):
        status = "✅" if self.done else "❌"
        print(f"{self.id_index}. {status}{self.task}")

def save_data(loaded_data):
    list_todo = []
    try:
        for new_task in loaded_data:
            list_todo.append({"name": new_task.task,
                              "id_index": new_task.id_index,
                              "done": new_task.done
                              })
        with open("todo_list.json", "w", encoding="utf-8") as f:
            json.dump(list_todo, f, ensure_ascii=False, indent=4)
    except FileNotFoundError:
        print("file not found!")

def load_data():
    object_todo = []
    try:
        with open("todo_list.json", "r", encoding="utf-8") as f:
            loaded_data = json.load(f)
        for item in loaded_data:
            todo = Todo(item["name"], item["id_index"], item["done"])
            object_todo.append(todo)
        return object_todo
    except FileNotFoundError:
        return []

def collect_todo_data(loaded_data):
    data = []
    while True:
        try:
            numbers = int(input("How many tasks would you like to add: "))
            if numbers <= 0:
                print("Add at least one task")
                continue
            for i in range(numbers):
                task = input("Enter task: ")
                id_index = len(loaded_data) + i + 1
                new_task = Todo(task, id_index)
                data.append(new_task)
            break
        except ValueError:
            print("Invalid value input!")
    return data

def show_all_tasks(loaded_data):
    print("=== TO DO LIST ===")
    for new_task in loaded_data:
        new_task.show()

def mark_as_done(loaded_data):
    try:
        for new_task in loaded_data:
            new_task.show()
        choice_done = int(input("Which task would you like to mark as done: "))
        for new_task in loaded_data:
            if choice_done == new_task.id_index:
                new_task.mark()
                save_data(loaded_data)
                return
    except ValueError:
        print("Invalid value input!")

def delete_tasks(loaded_data):
    try:
        for new_task in loaded_data:
            new_task.show()
        choice_delete = int(input("Which task task would you like to delete (select number): "))
        for new_task in loaded_data:
            loaded_data[:] = [item for item in loaded_data if choice_delete != item.id_index]
        for i, item in enumerate(loaded_data, start=1):
            item.id_index = i
        save_data(loaded_data)
    except ValueError:
        print("Invalid value input!")
    except IndexError:
        print("Invalid Index!")

def main():
    while True:
        try:
            loaded_data = load_data()
            print("\n=== TO-DO LIST ===")
            print("1. Show all tasks")
            print("2. Add task")
            print("3. Mark task as done")
            print("4. Delete task")
            print("5. Exit")
            choice = int(input("Your choice[1-5]: "))
            if choice < 1 or choice > 5:
                print("Invalid choice! Please try again.")
            elif choice == 1:
                show_all_tasks(loaded_data)
            elif choice == 2:
                new_task = collect_todo_data(loaded_data)
                loaded_data.extend(new_task)
                save_data(loaded_data)
            elif choice == 3:
                mark_as_done(loaded_data)
            elif choice == 4:
                delete_tasks(loaded_data)
            elif choice == 5:
                break
        except ValueError:
            print("Invalid value input!")

if __name__ == "__main__":
    main()