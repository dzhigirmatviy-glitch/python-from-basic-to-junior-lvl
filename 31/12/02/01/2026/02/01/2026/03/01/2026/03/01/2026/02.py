def get_one_shift():
    print("=== One shift ===")
    hours = int(input("hours: "))
    passengers = int(input("passengers: "))
    stress = int(input("stress(1-10): "))

    print(f"You worked {hours} hours")
    print(f"Served {passengers} passengers")
    print(f"Stressed {stress}/10")

    return hours, passengers, stress

result = get_one_shift()
print(f"Result: {result},")


def calculate_simple_efficiency(p, h):
    efficiency = p / h
    return efficiency

hours, passengers, stress = get_one_shift()

eff = calculate_simple_efficiency(passengers, hours)
print(f"Efficiency: {eff:.1f} pass/hour")

print("=== 3 DAY SHIFT TRACKER ===")

print("\nDay 1: ")
h1, p1, s2 = get_one_shift()
eff1 = calculate_simple_efficiency(p1, h1)
print(f"Day 1 efficiency: {eff1:.2f} pass/hour")

print("\nDay 2: ")
h2, p2, s3 = get_one_shift()
eff2 = calculate_simple_efficiency(p2, h2)
print(f"Day 2 efficiency: {eff2:.2f} pass/hour")

print("\nDay 3: ")
h3, p3, s4 = get_one_shift()
eff3 = calculate_simple_efficiency(p3, h3)
print(f"Day 3 efficiency: {eff3:.2f} pass/hour")

total_passengers = p1 + p2 + p3
total_hours = h1 + h2 + h3
average_eff = total_passengers / total_hours

print(f"\n=== SUMMARY ===")
print(f"Total passengers: {total_passengers}")
print(f"Total hours: {total_hours}")
print(f"Average efficiency: {average_eff:.2f} pass/hour")


