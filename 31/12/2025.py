days = int(input("how many days:  "))

hours = []
passengers = []
stressed = []
delayes = 0
max_passengers = 0
max_day = 0
max_stress = 0
stress_day = 0


for day in range(1, days + 1):
    print(f"day {day}")
    hour = int(input("how many hours did you work: "))
    hours.append(hour)

    passenger = int(input("how many passengers was: "))
    passengers.append(passenger)
    if passenger > max_passengers:
        max_passengers = passenger
        max_day = day

    stress = int(input("what`s your rate of stress(1-10): "))
    stressed.append(stress)
    if stress > max_stress:
        max_stress = stress
        stress_day = day

    delayed = input("was the flight delayed(yes/no): ")
    if delayed == "yes":
        delayes += 1


print("=== RESUME ===")
for day in range(1, days + 1):
    print(f" day {day}: {hours[day - 1]} hours, {passengers[day - 1]} passengers, stress {stressed[day - 1]}")

print("RESULT: ")
print(f"All hours: {sum(hours)}")
print(f"All passengers: {sum(passengers)}")
print(f"Middle stress: {sum(stressed) / len(stressed):.1f}")
print(f"All delayed: {delayes}\n")

print(f"EFFICIENCY: ")
for day in range(1, days + 1):
    print(f"day {day}: {passengers[day - 1] / hours[day - 1]:.1f} pass/hour\n")

print(f"THE MOST DIFFICULT DAY: day {max_day} ({max(passengers)} passengers)")

print(f"MAX STRESS: day {stress_day} (score {max(stressed)})")