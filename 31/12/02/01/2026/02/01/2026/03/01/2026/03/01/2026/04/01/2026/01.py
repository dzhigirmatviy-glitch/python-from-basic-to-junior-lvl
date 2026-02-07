def get_shift_day(day_number):
    print(f"day {day_number}: ")
    hours = int(input("how many work hours: "))
    passengers = int(input("how many passengers: "))
    stress = int(input("how many stress did you get(1/10): "))
    return hours, passengers, stress


def calculate_efficiency(passengers, hours):
    efficiency = passengers / hours
    return efficiency

def print_day_report(day, hours, passengers, stress, efficiency):
    print(f"\nreport day {day}: ")
    print(f"you worked {hours} hours")
    print(f"you got {passengers} passengers")
    print(f"your stress was {stress}/10")
    print(f"your efficiency is {efficiency:.1f} pass/hour")

def print_final_report(total_hours, total_passengers, total_efficiency):
    print(f"\n=== FINAL REPORT ===")
    print(f"total hours: {total_hours} hours")
    print(f"total passengers: {total_passengers} passengers")
    print(f"average efficiency: {total_efficiency:.1f} pass/hour")

h1, p1, s1 = get_shift_day(1)
eff1 = calculate_efficiency(p1, h1)
print_day_report(1, h1, p1, s1, eff1)

h2, p2, s2 = get_shift_day(2)
eff2 = calculate_efficiency(p2, h2)
print_day_report(2, h2, p2, s2, eff2)

h3, p3, s3 = get_shift_day(3)
eff3 = calculate_efficiency(p3, h3)
print_day_report(3, h3, p3, s3, eff3)

total_hours = h1 + h2 + h3
total_passengers = p1 + p2 + p3
avg_efficiency = (eff1 + eff2 + eff3) / 3

print_final_report(total_hours, total_passengers, avg_efficiency)
