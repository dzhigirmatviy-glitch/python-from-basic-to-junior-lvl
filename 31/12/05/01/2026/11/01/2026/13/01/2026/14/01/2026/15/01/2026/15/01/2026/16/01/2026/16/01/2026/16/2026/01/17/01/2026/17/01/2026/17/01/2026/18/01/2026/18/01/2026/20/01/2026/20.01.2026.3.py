import json
def add_habit_day(existing_habits):
    data = []
    start_number = existing_habits[-1]['id'] + 1 if existing_habits else 1
    while True:
        try:
            days = int(input("Input the number of days: "))
            for day_index in range(days):
                print(f"Day {day_index + 1}")
                id_index = start_number + day_index
                date = input("Input the date of the habit: ")
                numbers = int(input("How many habits would you like to add: "))
                comment = input("Input the comment of the habit: ")
                habits_dict = {}
                for habit_index in range(numbers):
                    habit = input("Input a habit: ")
                    done = input("have you done this habit? y/n: ")
                    if done == "y":
                        habits_dict[habit] = True
                    else:
                        habits_dict[habit] = False
                data.append({
                    "id": id_index,
                    "date": date,
                    "habits": habits_dict,
                    "comment": comment
                })
            break
        except ValueError:
            print("Invalid input of number. Please try again.")
    return data

def show_all_days(all_days):
    for data in all_days:
        print(f"{data['date']}")
        for habit, done in data['habits'].items():
            if done == True:
                print(f"{habit}: ✅")
            else:
                print(f"{habit}: ❌")

def calculate_statistic(all_days):
    all_habits = set()
    print("--- STATISTIC ---")
    print(f"All days considered: {len(all_days)}")
    for data in all_days:
        all_habits.update(data["habits"].keys())
    for habit in all_habits:
        done_yes = 0
        result = ""
        for data in all_days:
            done = data["habits"].get(habit, False)
            if done:
                done_yes += 1
                result += "✅"
            else:
                result += "❌"
        print(f"{habit}: {done_yes}/{len(result)} ({(done_yes / len(result)) * 100:.0f}%) {result}")

def save_habits_data(all_days):
    with open("habit_tracker.json", "w", encoding="utf-8") as f:
        json.dump(all_days, f, indent=4, ensure_ascii=False)

def load_data():
    while True:
        try:
            with open("habit_tracker.json", "r", encoding="utf-8") as f:
                return json.load(f)
        except FileNotFoundError:
            return []

loaded_data = load_data()
def main():
    while True:
        try:
            print("=== HABIT TRACKER ===")
            print("\n1. Add day with habits")
            print("2. Show all days with habits")
            print("3. Statistic by habits")
            print("4. Quit")
            choose = int(input("Choose your option[1-4]: "))
            if choose == 1:
                all_days = add_habit_day(loaded_data)
                loaded_data.extend(all_days)
                save_habits_data(loaded_data)
            elif choose == 2:
                show_all_days(loaded_data)
            elif choose == 3:
                calculate_statistic(loaded_data)
            elif choose == 4:
                print("Good bye!")
                break
        except ValueError:
            print("Invalid input of number. Please try again.")

if __name__ == "__main__":
    main()