days = int(input(f"Days of training (1-7): "))
if not (1 <= days <= 7):
    print("days must be between 1 and 7")

types = []
minutes = []
energies = []
type_count = 0
strong = 0
cardio = 0
max_minutes = 0
max_day = 0

for day in range(1, days + 1):
    print(f"\nday {day}: ")
    type = input("type (strong/cardio/rest): ")
    types.append(type)
    if type == "strong":
        strong += 1
    elif type == "cardio":
        cardio += 1

    minute = int(input("minutes: "))
    minutes.append(minute)

    energy = int(input("energy: "))
    energies.append(energy)

    if minute > max_minutes:
        max_minutes = minute
        max_day = day

print("=== RESULTS ===")
print(f"All time: {sum(minutes)} minutes")
print(f"strong: {strong}, cardio: {cardio}")
print(f"average energy: {sum(energies)/days}")
print(f"The longest: day {max_day} ({max_minutes} minutes)")






