import json
def main_mood_data():
    data = []
    days = int(input("how many days: "))
    for day in range(1, days + 1):
        while True:
            try:
                mood = int(input("mood(1-10): "))
                data.append({"day": day,
                             "mood": mood
                             })
                break
            except ValueError:
                print("set value number")
    return data

def saving_mood_data(main_data):
    try:
        with open("mood_data.json", "w", encoding="utf-8") as f:
            json.dump(main_data, f, ensure_ascii=False, indent=4)
    except FileNotFoundError:
        print("mood_data.json not exist")

def load_main_data():
    try:
        with open("mood_data.json", "r", encoding="utf-8") as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        print("mood_data.json not found")
        return []

def display_data(loaded_data):
    if not loaded_data:
        print("no data found...")
        return

    total_score = sum(day["mood"] for day in loaded_data)
    average_score = total_score / len(loaded_data)

    print("=== MOOD TRACKER ===")

    for day in loaded_data:
        print(f"{day['day']}: {day['mood']} score")
    print(f"total score: {total_score:.1f} score")
    print(f"average score: {average_score:.1f} score")

    best_day = 0
    best_score = 0

    for day in loaded_data:
        if day["mood"] > best_score:
            best_score = day["mood"]
            best_day = day["day"]

    print(f"best day {best_day}, {best_score} score")



if __name__ == "__main__":
    main_data = main_mood_data()
    if main_data:
        saving_mood_data(main_data)
        loaded_data = load_main_data()
        display_data(loaded_data)

