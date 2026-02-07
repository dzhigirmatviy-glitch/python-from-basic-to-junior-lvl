days = []
moods =[]

days = int(input("how many days: "))
for day in range(1, days + 1):
    print(f"day {day}")
    mood = int(input("your mood from 1 to 10: "))
    moods.append((day, mood))

for day in range(1, days + 1):
    print(f"day {day}: {moods[day-1][1]}")

total_score = 0
for day, amount in moods:
    total_score += amount

total_score_mid = total_score / days
print(f"middle score: {total_score_mid}")

max_score = 0
for day in moods:
    if day[1] > max_score:
        max_score = day[1]

print(f"the best day: day {day[0]}, score {max_score}")

if total_score_mid <= 3:
    print("the worst time, your middle score is below 7")
elif total_score_mid <= 7:
    print("normal time in your life, but can be better")
elif total_score_mid <= 10:
    print("the best time in your life!")
else:
    print("invalid number")