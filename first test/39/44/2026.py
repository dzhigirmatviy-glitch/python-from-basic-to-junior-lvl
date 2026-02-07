import json
from datetime import datetime
class Shifts:
    def __init__(self, date: datetime, start: float, end: float):
        self.date = date
        self.start = start
        self.end = end

    def to_list(self):
        return {"date": self.date.strftime("%Y-%m-%d"),
                "start": self.start,
                "end": self.end
                }
    @classmethod
    def to_obj(cls, data: dict):
        return cls(datetime.strptime(data["date"], "%Y-%m-%d"),
                   data["start"],
                   data["end"]
                   )

def save_data(shifts):
    with open("shifts.json", "w", encoding="utf-8") as f:
        json.dump([shift.to_list() for shift in shifts], f, ensure_ascii=False, indent=4)

def load_data():
    try:
        with open("shifts.json", "r", encoding="utf-8") as f:
            loaded_data = json.load(f)
            return [Shifts.to_obj(item) for item in loaded_data]
    except FileNotFoundError:
        print("File not found")
        return []

def evaluation_shifts_durations(loaded_data):
    durations_list = []
    all_hours = 0
    for shift in loaded_data:
        if shift.end > shift.start:
            duration = shift.end - shift.start
        else:
            duration = shift.end - shift.start + 24
        durations_list.append(duration)
        all_hours += duration
    return durations_list, all_hours

def evaluate_shift_longest(loaded_data):
    max_day = 0
    max_duration = 0
    for shift in loaded_data:
        if shift.end > shift.start:
            duration = shift.end - shift.start
        else:
            duration = shift.end - shift.start + 24
        if duration > max_duration:
            max_duration = duration
            max_day = shift.date
    return max_day, max_duration

