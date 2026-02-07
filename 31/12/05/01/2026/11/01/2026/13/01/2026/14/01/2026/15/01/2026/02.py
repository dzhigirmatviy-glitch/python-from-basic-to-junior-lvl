def get_reading_data():
    days = int(input("how many days: "))
    data = []
    for day in range(1, days + 1):
        while True:
            try:
                time = float(input("how long were you reading the book(min): "))
                pages = float(input("how many pages were you reading: "))
                data.append({
                    "day": day,
                    "minutes": time,
                    "pages": pages
                })
                break
            except ValueError:
                print("Please enter a valid number")
    return data

def calculate_total(reading_data):
    total_minutes = 0
    total_pages = 0
    for entry in reading_data:
        time = entry["minutes"]
        pages = entry["pages"]
        total_minutes += time
        total_pages += pages
    return total_minutes, total_pages

def calculate_pages_per_minutes(total_all):
    return total_all[1] / total_all[0]

def find_best_reading_day(reading_data):
    max_day = 0
    max_pages = 0
    for entry in reading_data:
        pages = entry["pages"]
        day = entry["day"]
        if pages > max_pages:
            max_pages = pages
            max_day = day
    return max_day, max_pages

def print_reading_report(reading_data, total_all, pages_per_minutes, best_day):
    print("=== WEEKLY READING REPORT ===")
    for entry in reading_data:
        time = entry["minutes"]
        pages = entry["pages"]
        day = entry["day"]
        print(f"day {day}: {time} min, {pages} pages")
    print(f"\n=== SUMMARY ===")
    print(f"total reading time: {total_all[0]} min")
    print(f"total pages read: {total_all[1]} pages")
    print(f"reading speed: {pages_per_minutes:.2f} pages/minutes")
    print(f"best reading day: day {best_day[0]} ({best_day[1]} pages)")

import json
def save_data(reading_data, total_all, pages_per_minutes, best_day):
    report = {"daily_reading": reading_data,
              "total": {"minutes": total_all[0],
                        "pages": total_all[1]
                        },
              "pages_per_minutes": pages_per_minutes,
              "best_day": {"day": best_day[0],
                           "pages": best_day[1]
                           }
    }
    with open('reading_data.json', 'w', encoding='utf-8') as f:
        json.dump(report, f, indent=4, ensure_ascii=False)
    return report

import json
def load_data(file_data):
    while True:
        try:
            with open(file_data, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"File {file_data}  not found")
            return None
        except json.JSONDecodeError:
            print(f"Error in reading file {file_data}. file damaged")
            return None

def main_menu():
    print("\n=== READING TRACKER ===")
    print("1. Add new data")
    print("2. Look history")
    print("3. Show statistic")
    print("4. Exit")

    choice = input("Enter option(1-4): ")
    return choice

import json
def show_history(file_data):
    data = load_data(file_data)
    if data is None:
        print("No history found")
        return
    print("\n=== READING HISTORY ===")

    for entry in data.get("daily_reading", []):
        day = entry.get("day", 0)
        minutes = entry.get("minutes", 0)
        pages = entry.get("pages", 0)
        print(f"day {day}: {minutes} min, {pages} pages")

    if "total" in data:
        print(f"\nTotal: {data['total'].get('minutes', 0)} min, "
              f"({data['best_day'].get('pages', 0)} pages)
              )

    if "best_day" in data:
        print(f"\nBest day: {data['best_day'].get('day', 0)} "
              f"({data['best_day'].get('pages', 0)} pages)"
              )

import json
def main():
    file_data = "reading_data.json"
    while True:
        try:
            choice = main_menu()
            if choice == 1:
                reading_data = get_reading_data()
                total_all = calculate_total(reading_data)

                best_day = find_best_reading_day(reading_data)

                save_data(reading_data, total_all, pages_per_minutes, best_day)

            elif choice == 2:
                show_history(file_data)

            elif choice == 3:
                data = load_data(file_data)
                if data and "daily_reading" in data:
                    reading_data = data["daily_reading"]
                    total_all = calculate_total(reading_data)
                    best_day = find_best_reading_day(reading_data)
                    print_reading_report(reading_data,
                                         total_all,
                                         pages_per_minutes,
                                         best_day
                    )
                else:
                    print("No data")

            elif choice == 4:
                print("Goodbye")
                break
            else:
                print("Invalid Choice")

if __name__ == "__main__":
    reading_data = get_reading_data()
    total_all = calculate_total(reading_data)
    pages_per_minutes = calculate_pages_per_minutes(total_all)
    best_day = find_best_reading_day(reading_data)

    print_reading_report(reading_data,
                         total_all,
                         pages_per_minutes,
                         best_day
    )

    file_data = save_data(reading_data, total_all, pages_per_minutes, best_day)
    main()