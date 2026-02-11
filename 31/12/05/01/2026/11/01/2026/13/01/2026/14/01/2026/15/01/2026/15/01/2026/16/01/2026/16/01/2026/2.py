import json
def main_fitnes_data():
    data = []
    days = int(input("how many days: "))
    for day in range(1, days + 1):
        while True:
            try:
                calories = float(input("calories burned: "))
                data.append({"day": day,
                             "calories": calories
                             })
                break
            except ValueError:
                print("please set valid number")
    return data

def saving_fitnes_data(main_data):
    try:
        with open("fitnes_data.json", "w", encoding="utf-8") as f:
            json.dump(main_data, f, ensure_ascii=False, indent=4)
        return True
    except Exception as e:
        print(f"Error saving data: {e}")
        return False

def load_fitnes_data():
    try:
        with open("fitnes_data.json", "r", encoding="utf-8") as f:
            data = json.load(f)
        print(f"succsesfully loaded {len(data)} records")
        return data
    except FileNotFoundError:
        print(f"fitnes_data.json not found")
        return []

def display_statistics(data):
    if not data:
        print("no data")
        return

    total_calories = sum(day["calories"] for day in data)
    average = total_calories / len(data)

    print("=== FITNESS STATISTICS ===")

    for day in data:
        print(f"day {day['day']}: {day['calories']} calories")

    print(f"total calories burned: {total_calories:.1f}")
    print(f"average calories burned: {average:.1f}")



if __name__ == "__main__":
    main_data = main_fitnes_data()
    if main_data:
        saving_fitnes_data(main_data)
        loaded_data = load_fitnes_data()
        display_statistics(loaded_data)

