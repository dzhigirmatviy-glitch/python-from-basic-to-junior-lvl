coffies = []
days = []

days = int(input("how many days in week: "))
for day in range(1, days + 1):
    print(f"\n day {day}")
    coffe = int(input("how many cups of coffe did you drink: "))
    coffies.append((day, coffe))

total_coffe = 0
for day, amount in coffies:
    total_coffe += amount

if total_coffe >= 20:
    print(f"too much coffe!")
elif total_coffe < 10:
    print(f"take another one cup of coffe!")
else:
    print("perfect quanity of coffe!")
