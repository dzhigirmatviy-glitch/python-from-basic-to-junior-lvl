def get_daily_expense():
    data = []
    days = int(input("set how many days: "))
    for day in range(1, days + 1):
        while True:
            try:
                print(f"day {day}: ")
                expense = float(input("set how much expenses: "))
                data.append([day, expense])
                break
            except ValueError:
                print("Invalid number!")
    return data

daily_expense = get_daily_expense()

def calculate_total(daily_expense):
    total = 0
    for day, expense in daily_expense:
        total += expense
    return total

total_expense = calculate_total(daily_expense)

def average_expense(total_expense, daily_expense):
    average = total_expense / len(daily_expense)
    return average

average_expense = average_expense(total_expense, daily_expense)

def find_max_day(daily_expense):
    max_day = 0
    max_expense = 0
    for day, expense in daily_expense:
        if expense > max_expense:
            max_expense = expense
            max_day = day
    return max_day, max_expense

print(find_max_day(daily_expense))
