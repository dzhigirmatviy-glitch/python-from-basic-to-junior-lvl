def get_training_data():
    data = []
    days = int(input("set how many days you trained: "))
    for day in range(1, days + 1):
        while True:
            try:
                print(f"day {day}")
                time = float(input("set how many time you trained (min): "))
                calories = float(input("set how many calories you lost: "))
                data.append([day, time, calories])
                break
            except ValueError:
                print("set value number!")
    return data

training_data = get_training_data()

def calculate_total_time(training_data):
    total_time = 0
    for day, time, calories in training_data:
        total_time += time
    return total_time

tot_time = calculate_total_time(training_data)

def calculate_total_calories(training_data):
    total_calories = 0
    for day, time, calories in training_data:
        total_calories += calories
    return total_calories

tot_calories = calculate_total_calories(training_data)

def calculate_average_calories(tot_calories, training_data):
    average_cal = tot_calories / len(training_data)
    return average_cal

average_calories = calculate_average_calories(tot_calories, training_data)

def calculate_average_day(tot_time, training_data):
    average = tot_time / len(training_data)
    return average

average_time = calculate_average_day(tot_time, training_data)

def find_best_day(training_data):
    best_day = 0
    best_calories = 0
    for day, time, calories in training_data:
        if calories > best_calories:
            best_calories = calories
            best_day = day
    return best_day, best_calories

best_day_data = find_best_day(training_data)

def print_training_report(training_data, tot_time, tot_calories, average_calories, average_time, best_day_data):
    for day, time, calories in training_data:
        print(f"day {day}: {time} min, {calories} cal")
    print("=== SUMMARY ===")
    print(f"total training time: {tot_time:.1f} min")
    print(f"total calories burned: {tot_calories:.1f} cal")
    print(f"average per day: {average_time:.1f} min and {average_calories:.1f} cal")
    print(f"best day training: day {best_day_data[0]} ({best_day_data[1]} cal) ")

print_training_report(training_data, tot_time, tot_calories, average_calories, average_time, best_day_data)