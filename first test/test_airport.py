from datetime import datetime
from airport import find_the_longest_shift
from airport import Airport
def test_airport_creation():
    date = datetime(2024, 1, 1)
    start = 5.5
    end = 13.5
    shift_type = "Morning"

    shift = Airport(date, start, end, 8.0, shift_type, "No incidents", 80.0)

    assert shift.date == date
    assert shift.start == start
    assert shift.end == end
    assert shift.shift_type == shift_type
    assert shift.salary == 80.0

def test_find_the_longest_shift_bug():
    shifts = [
        Airport(datetime(2024,1,1), 5.5, 13.5, 8.0, "Morning", "No incidents", 80.0)
    ]
    date, duration = find_the_longest_shift(shifts)

    print(f"Result of function: date={date}, duration={duration}")
    print(f"Expected: date=2024-01-01, duration=8.0")

    assert date == datetime(2024, 1, 1)
    assert duration == 8.0