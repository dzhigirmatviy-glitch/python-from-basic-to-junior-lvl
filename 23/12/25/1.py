hours = []
trips =[]

days = int(input("how many worker days: "))

for day in range(1, days + 1):
    print(f"\nday {day}")
    hour = int(input(f"hours: "))
    hours.append((day, hour))
    trip = int(input(f"flight: "))
    trips.append((day, trip))

total1 = 0
for day, amount in hours:
    total1 += amount

total2 = 0
for day, amount in trips:
    total2 += amount

dayx = total1 / days
flightx = total2 / days

print("\n=== RESULTS ===")
print(f"all hours: {total1}")
print(f"all flights: {total2}")
print(f"middle per day: {dayx:.1f} hours, {flightx:.1f} flights")

max = 0
for day in trips:
    if day[1] > max:
        max = day[1]

work = 0
for day in hours:
    if day[1] > work:
        work = day[1]

print(f"the most difficult day: day {day[0]} ({max} flights) and {work:.1f} hours")

if dayx >= 8:
    print(f"RESULT: Ower working! (>{dayx} hours in middle per day)")

