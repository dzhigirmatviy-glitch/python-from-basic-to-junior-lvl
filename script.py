num1 = float(input("set first number:"))
operator = input("select operation: (+, -, *, /): ")
num2 = float(input("set second number: "))

if operator == "+":
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
elif operator == "-":
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
elif operator == "*":
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
else:
    result = num1 / num2
    print(f"{num1} / {num2} = {result}")

if result < 0:
    print(f"analys: below zero")
elif result < 100:
    print(f"analys: middle number")
elif result >= 100:
    print(f"analys: high number")
else:
    print(f"analys: error division by zero!")

history = []

if result is not None:
    history.append(f"{num1} {operator} {num2} = {result}")
print("\n" + "=" * 30)
print("operation history")
print("=" * 30)
if len(history) > 0:
    for i, operation in enumerate(history, 1):
        print(f"{i}, {operation}")


