days = []
productivities = []
goals = []
n_goals = []

days = int(input("how many days analysed: "))
for day in range(1, days + 1):
    productivity = int(input(f"What`s your score of productivity in day {day}: "))
    goal = input(f"Did you have any goals in day {day} (yes/no): ")
    if productivity < 0:
        print("It`s can`t be below zero!")
    elif productivity > 10:
        print("it`s can`t be above ten!")
    productivities.append((day, productivity))
    goals.append((day, goal))
    if goal == "yes":
        n_goal = 1
        n_goals.append((day, n_goal))

num_goal = 0
for day, amount in n_goals:
    num_goal += amount

for day in range(1, days + 1):
    print(f"day {day}:\n Productivity score(1-10): {productivities[day - 1][1]}\n Had any goals? (yes/no): {goals[day - 1][1]} ")


max_productivities = 0
num_days = 0

for day_nums, productivity in productivities:
    if productivity > max_productivities:
        max_productivities = productivity
        num_days = day_nums

print("=== RESULTS ===")
print(f"All scores:")
for day in range(1, days + 1):
    print(f"[{productivities[day - 1][1]}];")

sum_productivities = 0
for day, amount in productivities:
    sum_productivities += amount
mid_sum_productivities = sum_productivities / days

print(f"Middle Productivity score: {mid_sum_productivities:.1f}")

print(f"Days with goals: {num_goal} from {days}")

print(f"The most productive day: day {num_days} (score {max_productivities})")






