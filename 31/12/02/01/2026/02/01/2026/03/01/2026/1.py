def get_shift_data(hours, passengers, stress):
    hours = int(input("work hours: "))
    passengers = int(input("s#passengers: "))
    stress = int(input("stress(1-10): "))
    return hours, passengers, stress

def calculate_efficiency(passengers, hours):
    efficiency = passengers / hours
    print(f"efficiency: {efficiency:.1f} pass/hour")
    return efficiency

def evaluate_shift(day, passengers, hours, stress):
    day = int(input("work day: "))
    print(f"Day {day}: ")
    shift = get_shift_data(hours, passengers, stress)
    efficiency_day = calculate_efficiency(passengers, hours)
    average_efficiency = sum(efficiency_day) / sum(day)
    print(f"SUMARY: \naverage_efficiency: {average_efficiency:.1f} pass/hour")
    return shift, efficiency_day, average_efficiency, day

evaluate_shift(1, 300, 6, 7)
print("---")
evaluate_shift(2, 600, 9, 9)
print("---")
evaluate_shift(3, 800, 4, 6)