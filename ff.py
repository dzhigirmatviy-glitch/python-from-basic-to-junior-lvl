expenses = []
days = ["monday", "tuesday", "wendnesday"]
for day in days:
    expense = float(input(f"enter expense for {day}: $"))
    expenses.append((day, expense))

print("\n" + "="*40)
print("history of expenses")
print("="*40)

total = 0
for day, amount in expenses:
    print(f"{day}: {amount:.2f}$")
    total += amount

print("\n" + "-"*40)
print(f"total for a week: {total:.2f}")
print(f"mediana of the week: {total/3:.2f}")

