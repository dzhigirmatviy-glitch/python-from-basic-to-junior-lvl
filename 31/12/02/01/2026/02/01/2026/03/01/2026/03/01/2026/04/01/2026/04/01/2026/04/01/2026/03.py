def ask_number():
    number = int(input("your number: "))
    return number

def double_it(x):
    result = x * 2
    return result

def print_result(y):
    print(f"===RESULT===")
    print(f"double number: {y}")


my_number = ask_number()
doubled = double_it(my_number)
print_result(doubled)