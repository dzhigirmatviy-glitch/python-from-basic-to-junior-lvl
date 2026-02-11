import json
def add_tasks(existing_tasks):
    data = []
    start_number = existing_tasks[-1]['number'] + 1 if existing_tasks else 1
    numbers = int(input("Please input the number of tasks: "))
    for i in range(numbers):
        number = start_number + i
        task = input("Please input the tasks: ")
        done = input("[y/n]: ")
        data.append({"number": number,
                     "task": task,
                     "done": done
        })
    return data

def show_all_tasks(tasks):
    for task in tasks:
        if task["done"] == "y":
            print(f"task number {task['number']}: {task['task']} [✓]")
        else:
            print(f"task number {task['number']}: {task['task']} [x]")

def save_tasks(tasks):
    with open("todo_list.json", "w", encoding="utf-8") as f:
        json.dump(tasks, f, ensure_ascii=False, indent=4)

def load_tasks():
    try:
        with open("todo_list.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

tasks = load_tasks()


def delete_tasks(tasks):
    show_all_tasks(tasks)
    number_to_delete = int(input("\ninput the number to delete: "))

    tasks[:] = [task for task in tasks if task["number"] != number_to_delete]
    save_tasks(tasks)

def main():
    while True:
        try:
            print("=== TODO LIST ===")
            print("1. Show all tasks")
            print("2. Add tasks and select condition")
            print("3. Delete tasks")
            print("4. Exit")
            action = int(input("\nplease select the action[1-5]: "))
            if action == 1:
                show_all_tasks(tasks)
            elif action == 2:
                new_tasks = add_tasks(tasks)
                tasks.extend(new_tasks)
                save_tasks(tasks)
            elif action == 3:
                delete_tasks(tasks)
            else:
                break
        except ValueError:
            print("please input just numbers!")


main()