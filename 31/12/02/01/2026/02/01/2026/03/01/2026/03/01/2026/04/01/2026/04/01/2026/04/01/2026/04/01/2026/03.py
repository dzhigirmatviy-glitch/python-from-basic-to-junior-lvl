def get_age():
    age = int(input("your age: "))
    return age

my_age = get_age()

def check_alcohol(age):
    if age < 18:
        return False
    else:
        return True

my_check_alcohol = check_alcohol(my_age)

def print_permission(result):
    if result == True:
        print("Status: Allowed")
    else:
        print("Status: Denied")

print_permission(my_check_alcohol)