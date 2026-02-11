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