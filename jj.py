days = ["monday", "tuesday", "wednesday"]
earns =[]
base = 10
for day in days:
    earn = float(input(f"{day}: how many hours did you work: "))
    earns.append(days, earn)
amount = base * earn
for day, amount in earns:
    print(f"{day}: {amount:.2f} * {base}")


