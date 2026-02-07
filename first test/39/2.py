import json
class Fitness:
    def __init__(self, calories: float, training: str, minutes: float, type: str, number: int, done=False):
        self.calories = calories
        self.training = training
        self.minutes = minutes
        self.type = type
        self.number = number
        self.done = done

    def show(self):
        status = "✅" if self.done else "❌"
        print(f"{self.number}. {status} {self.type} {self.training} [{self.calories} cal. - {self.minutes} min.]")

    def mark_done(self):
        self.done = True

def save_data(loaded_data):
    list_fitness = []
    try:
        for new_fitness in loaded_data:
            list_fitness.append({"calories": new_fitness.calories,
                                "training": new_fitness.training,
                                 "minutes": new_fitness.minutes,
                                 "type": new_fitness.type,
                                 "number": new_fitness.number,
                                 "done": new_fitness.done
                                 })
        with open("fitness_data.json", "w", encoding="utf-8") as f:
            json.dump(list_fitness, f, ensure_ascii=False, indent=4)
    except FileNotFoundError:
        print("Fitness file not found.")

def load_data():
    obj_fitness = []
    try:
        with open("fitness_data.json", "r", encoding="utf-8") as f:
            loaded_data = json.load(f)
        for item in loaded_data:
            obj = Fitness(item["calories"], item["training"], item["minutes"], item["type"], item["number"], item["done"])
            obj_fitness.append(obj)
        return obj_fitness
    except FileNotFoundError:
        return []

def show_data(loaded_data):
    print("===ALL TRAININGS===")
    for obj_fitness in loaded_data:
        obj_fitness.show()

def mark_as_done(loaded_data):
    try:
        for obj_fitness in loaded_data:
            obj_fitness.show()
        choice_done = int(input("Select number to mark as done: "))
        for obj_fitness in loaded_data:
            if choice_done == obj_fitness.number:
                obj_fitness.mark_done()
                save_data(loaded_data)
                return
    except ValueError:
        print("Invalid input. Please try again.")

def delete_fitness(loaded_data):
    try:
        for obj_fitness in loaded_data:
            obj_fitness.show()
        choice_delete = int(input("Select number to delete: "))
        loaded_data[:] = [item for item in loaded_data if obj_fitness.number != choice_delete]
        for i, item in enumerate(loaded_data, start=1):
            item.number = i
        save_data(loaded_data)
    except ValueError:
        print("Invalid input. Please try again.")
    except IndexError:
        print("Invalid index. Please try again.")

def collect_fitness_data(loaded_data):
    data = []
    while True:
        try:
            numbers = int(input("how many trainings would you like to add: "))
            if numbers < 1 or numbers > 100:
                print("Invalid input. Please input a number between 1 and 100.")
            for i in range(numbers):
                calories = float(input("How many calories you burned or gonna burn: "))
                training = input("Input your exercise: ")
                minutes = float(input("Input how many minutes you was training: "))
                type = input("Input the type of you exercise: ")
                number = len(loaded_data) + i + 1
                done = False
                new_fitness = Fitness(calories, training, minutes, type, number, done)
                data.append(new_fitness)
            break
        except ValueError:
            print("Invalid input. Please try again.")
    return data

def statistics(loaded_data):
    def evaluate_fitness_statistic():
        all_time = 0
        all_calories = 0
        for obj_fitness in loaded_data:
            all_time += obj_fitness.minutes
            all_calories += obj_fitness.calories
        return all_time, all_calories
    all_time, all_calories = evaluate_fitness_statistic()
    print("=== TRAINING STATISTIC ===")
    for obj_fitness in loaded_data:
        obj_fitness.show()
    print("\n--- GENERAL ---")
    print(f"All time: {all_time} minutes")
    print(f"All calories burned: {all_calories} calories.")

def main():
    while True:
        try:
            loaded_data = load_data()
            print("\n=== FITNESS TRACKER ===")
            print("1. Add training")
            print("2. Show all trainings")
            print("3. Show training statistics")
            print("4. Delete training")
            print("5. Mark training as done")
            print("6. Exit")
            choice = int(input("Select number: "))
            if choice == 1:
                new_fitness = collect_fitness_data(loaded_data)
                loaded_data.extend(new_fitness)
                save_data(loaded_data)
            elif choice == 2:
                show_data(loaded_data)
            elif choice == 3:
                statistics(loaded_data)
                save_data(loaded_data)
            elif choice == 4:
                delete_fitness(loaded_data)
            elif choice == 5:
                mark_as_done(loaded_data)
            elif choice == 6:
                break
        except ValueError:
            print("Invalid input. Please try again.")

if __name__ == "__main__":
    main()