days = []
hours = []
passengers = []
incidents = []
effective_passengers = []
qualities = []

days = int(input(f"how many days you worked: "))
for day in range(1, days + 1):
    print(f"day {day}")
    hour = float(input(f"how many hours did you work in day {day}: "))
    passenger = int(input(f"how many passengers was in day {day}: "))
    incident = int(input(f"how many incidents was in day {day}: "))
    hours.append((day, hour))
    passengers.append((day, passenger))
    incidents.append((day, incident))

print("=== analys of efficiency ===")
for day in range(1, days + 1):
    effective_passenger = (passengers[day - 1][1] / hours[day - 1][1])
    effective_passengers.append((day, effective_passenger))
    print(f"day {day}: {effective_passengers[day -1][1]} pass/hour")
    quality = (((passengers[day - 1][1]) - (incidents[day - 1][1])) / (passengers[day - 1][1])) * 100
    if quality < 0:
        print("error")
    qualities.append((day, quality))
    print(f"day {day}: quality {qualities[day - 1][1]}%")

middle_passengers = 0
for day, amount in passengers:
    middle_passengers += amount
mid_middle_passengers = middle_passengers / days

middle_qualities = 0
for day, amount in qualities:
    middle_qualities += amount
mid_middle_qualities = middle_qualities / days

best_day = 0
pass_quality = 0

for day_num, passenger in effective_passengers:
    if passenger > pass_quality:
        pass_quality = passenger
        best_day = day_num


pass_qual = 0
qual_day = 0

for day_nums, incident in qualities:
    if incident > pass_qual:
        pass_qual = incident
        qual_day = day_nums

print(f"\n === RESUME ===")

print(f"middle quality: {mid_middle_qualities}%")
print(f"middle efficiency: {mid_middle_passengers} pass/hour")
print(f"\n")
print(f"the most efficiency: days {best_day}, ({pass_quality} pass/hour)")
print(f"the best quality: days {qual_day}, ({pass_qual}%)")






