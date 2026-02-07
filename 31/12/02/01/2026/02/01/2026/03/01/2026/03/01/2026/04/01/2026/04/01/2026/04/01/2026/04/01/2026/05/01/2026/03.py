def collect_shift_data():
    data = []
    hours = int(input("Enter hours: "))
    passengers = int(input("Enter passengers: "))
    stress = int(input("Enter stress: "))
    data.append([hours, passengers, stress])
    return data

my_data = collect_shift_data()
def analyze_shifts(data):
    for hours, passengers, stress in data:
        efficiency = (passengers / hours)
    return efficiency

my_efficiency = analyze_shifts(my_data)

def give_recommendations(efficiency):
    if efficiency > 50:
        return "Good Shift"
    elif efficiency > 30:
        return "Normal Shift"
    else:
        return "Bad Shift"

my_recommendations = give_recommendations(my_efficiency)

def print_report(my_efficiency, my_recommendations):
    print(f"Your efficiency: {my_efficiency:.1f} pass/hour")
    print(f"Recommendations: {my_recommendations}")

print_report(my_efficiency, my_recommendations)










def salary_shift(shift_data):
    for shift, hour, salary in shift_data:
        regular_pay = shift_data[shift - 1][1] * shift_data[shift - 1][2]
    return regular_pay






def over_time(shift_data):
    for shift, hour, salary in shift_data:
        over_work = hour - 8
    return over_work

over_work_shift = over_time(shift_data)