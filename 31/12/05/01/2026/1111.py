days = int(input("set your day numbers: "))
hours = []
for day in range(1, days + 1):
    print(f"day {day}")
    hour = int(input("how many hours did you spend: "))
    hours.append(hour)

print(f"total hours: {sum(hours)} hours")
print(f"average hours: {sum(hours) / len(hours):.2f} hours")


