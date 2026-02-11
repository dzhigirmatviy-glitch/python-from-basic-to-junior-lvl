import json
from datetime import datetime
def collect_health_data(existing_data):
    data = []
    while True:
        try:
            start_number = existing_data[-1]['id'] + 1 if existing_data else 1
            days = int(input("how many days you want to add: "))
            for i in range(days):
                id_index = start_number + i
                print(f"Day {id_index}: ")
                while True:
                        date_str = input("input your date YYYY-MM-DD: ")
                        try:
                            date = datetime.strptime(date_str, "%Y-%m-%d").date()
                            break
                        except ValueError:
                            print("Please input a valid date!")
                weight = float(input("Input your weight(kg): "))
                hours = float(input("Input how many hours did you sleep: "))
                steps = int(input("Input how many steps you did today: "))
                condition = int(input("Input your condition today (1-10): "))
                if not 1<=condition<=10:
                    print("Please input a valid condition! 1-10")
                    continue
                step_index=False
                data.append({"id": id_index,
                             "date": date,
                             "weight": weight,
                             "hours": hours,
                             "steps": steps,
                             "condition": condition,
                             "step_index": step_index
                })
            break
        except ValueError:
            print("Please input a valid number!")
        except IndexError:
            return []
    return data

def save_health_data(health_data):
    for data in health_data:
        data['date'] = data['date'].isoformat()
    with open("health_data.json", "w", encoding="utf-8") as f:
        json.dump(health_data, f, ensure_ascii=False, indent=4)

def load_health_data():
    try:
        with open("health_data.json", "r", encoding="utf-8") as f:
            data_list = json.load(f)
            for data in data_list:
                data['date'] = datetime.strptime(data['date'], "%Y-%m-%d").date()
        return data_list
    except FileNotFoundError:
        return []

def show_health_history(health_data):
    print("=== HEALTH HISTORY ===")
    for data in health_data:
        if data['step_index'] == True:
            print(f"\ndata{data['date']}")
            print(f"Your weight: {data['weight']} kg")
            print(f"Your hours of sleep: {data['hours']} hours")
            print(f"Your steps: {data['steps']} steps ✅")
            print(f"Your condition: {data['condition']}")
            print("--------------------------------------")
        elif data['step_index'] == False:
            print(f"\ndata{data['date']}")
            print(f"Your weight: {data['weight']} kg")
            print(f"Your hours of sleep: {data['hours']} hours")
            print(f"Your steps: {data['steps']} steps ❌")
            print(f"Your condition: {data['condition']}")
            print("--------------------------------------")

def mark_your_daily_goal(health_data):
    show_health_history(health_data)
    while True:
        choice = input("input date for mark you goal done YYYY-MM-DD: ")
        try:
            date = datetime.strptime(choice, "%Y-%m-%d").date()
            break
        except ValueError:
            print("Please input a valid date!")
        continue
    for data in health_data:
        if data['date'] == date:
            goal = input(f"Did you do 10000 steps? (y/n): ").lower().strip()
            if goal == "y":
                data['step_index']=True
            elif goal == "n":
                data['step_index']=False
            return

def evaluate_health_statistic(health_data):
    if not health_data:
        print("No health data!")
        return
    def evaluate_middle_weight():
        sum_weight = 0
        for data in health_data:
            sum_weight += data['weight']
        middle_weight = sum_weight / len(health_data)
        return middle_weight
    def evaluate_middle_hours():
        sum_hours = 0
        for data in health_data:
            sum_hours += data['hours']
        middle_hours = sum_hours / len(health_data)
        return middle_hours
    def evaluate_all_steps():
        sum_steps = 0
        for data in health_data:
            sum_steps += data['steps']
        return sum_steps
    def evaluate_middle_condition():
        sum_condition = 0
        for data in health_data:
            sum_condition += data['condition']
        middle_condition = sum_condition / len(health_data)
        return middle_condition
    def find_the_best_day():
        best_day = health_data[0]['date']
        best_score = health_data[0]['condition']
        for data in health_data:
            if data['condition'] > best_score:
                best_score = data['condition']
                best_day = data['date']
        return best_day, best_score
    best_day, best_score = find_the_best_day()

    print("=== STATISTIC HEALTH RESULT ===")
    print(f"The best day is {best_day}: {best_score} score")
    print(f"Middle weight: {evaluate_middle_weight()} kg")
    print(f"Middle hours: {evaluate_middle_hours()} hours")
    print(f"All steps: {evaluate_all_steps()} steps")
    print(f"Middle condition: {evaluate_middle_condition()}")

def main():
    while True:
        try:
            loaded_data = load_health_data()
            print("=== MAIN MENU OF YOUR TRACKER ===")
            print("\n1. Add new days with health data")
            print("2. Show all history")
            print("3. Statistic of health")
            print("4. Mark goal done")
            print("5. Exit")
            choice_menu = int(input("input your choice: "))
            if choice_menu == 1:
                health_data = collect_health_data(loaded_data)
                loaded_data.extend(health_data)
                save_health_data(loaded_data)
            elif choice_menu == 2:
                show_health_history(loaded_data)
            elif choice_menu == 3:
                evaluate_health_statistic(loaded_data)
            elif choice_menu == 4:
                mark_your_daily_goal(loaded_data)
                save_health_data(loaded_data)
            elif choice_menu == 5:
                break
        except ValueError:
            print("Please input a valid number!")
if __name__ == "__main__":
    main()




