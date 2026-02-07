import json
from datetime import datetime
class Airport:
    def __init__(self, date: datetime, start: float, end: float, duration: float, shift_type: str, incidents: str, salary: float):
        self.date = date
        self.start = start
        self.end = end
        self.duration = duration
        self.shift_type = shift_type
        self.incidents = incidents
        self.salary = salary

    def show(self):
        print(f"{self.date}| ({self.start} hours), ({self.end} hours), {self.shift_type}... {self.incidents}")

    def to_dict(self):
        return {"date": self.date.isoformat(),
                "start": self.start,
                "end": self.end,
                "duration": self.duration,
                "shift_type": self.shift_type,
                "incidents": self.incidents,
                "salary": self.salary
                }
    @classmethod
    def to_object(cls, data: dict):
        return cls(datetime.fromisoformat(data["date"]),
                   data["start"],
                   data["end"],
                   data["duration"],
                   data["shift_type"],
                   data["incidents"],
                   data["salary"]
        )

def save_data(shifts):
    with open("airport_shifts.json", "w", encoding="utf-8") as f:
        json.dump([shift.to_dict() for shift in shifts], f, ensure_ascii=False, indent=4)

def load_data():
    try:
        with open("airport_shifts.json", "r", encoding="utf-8") as f:
            loaded_data = json.load(f)
        return [Airport.to_object(item) for item in loaded_data]
    except FileNotFoundError:
        print("File not found")
        return []

def add_shift(loaded_data):
    data = []
    while True:
        try:
            days = int(input("How many days would you like to add: "))
            if days < 1:
                print("Invalid input. Please add at least one day")
                continue
            for i in range(days):
                date_str = input("Enter date (YYYY-MM-DD): ")
                date = datetime.fromisoformat(date_str)
                start = float(input("Enter start of your shift: "))
                if start < 0:
                    print("Invalid input. Please enter a positive number")
                elif start > 23.59:
                    print("Invalid input. Please enter number below 24")
                end = float(input("Enter end of your shift: "))
                if end < 0:
                    print("Invalid input. Please enter a positive number")
                elif end > 23.59:
                    print("Invalid input. Please enter number below 24")
                shift_type = input("Input type of your shift (Morning/Night): ")
                incidents = input("Input some note or incidents that were during your shift: ")
                salary_hour = float(input("Enter your shift salary per hour: "))
                if end >= start:
                    duration = end - start
                else:
                    duration = 24 - start + end
                salary = salary_hour * duration
                data.append(Airport(date, start, end, duration, shift_type, incidents, salary))
            break
        except ValueError:
            print("Invalid input. Please try again.")
    return data

def show_all_shifts(loaded_data):
    for shifts in loaded_data:
        shifts.show()

def find_the_longest_shift(loaded_data):
    if not loaded_data:
        return None, 0
    max_day = 0
    max_duration = 0
    for shift in loaded_data:
        if shift.duration > max_duration:
            max_duration = shift.duration
            max_day = shift.date
    return max_day, max_duration

def main():
    loaded_data = load_data()
    while True:
        try:
            print("=== AIRPORT SHIFT ANALYZER ===")
            print("1. Add shift")
            print("2. Show all shifts")
            print("3. Find the longest shift")
            print("4. Exit the program")
            choice = int(input("Select an option: "))
            if choice == 1:
                shifts = add_shift(loaded_data)
                loaded_data.extend(shifts)
                save_data(loaded_data)
            elif choice == 2:
                show_all_shifts(loaded_data)
            elif choice == 3:
                max_day, max_duration = find_the_longest_shift(loaded_data)
                print(f"The longest day was: {max_day} {max_duration}")
            elif choice == 4:
                break
        except ValueError:
            print("Invalid input. Please try again.")

if __name__ == "__main__":
    main()
