def data():
    while True:
        try:
            age = int(input("enter your age: "))
            experience = int(input("enter your experience: "))
            return age, experience
        except ValueError:
            print("please set value number")

age, experience = data()

def evaluate_age(age, experience):
    return age - experience

start_age = evaluate_age(age, experience)

def print_report(age, experience, start_age):
    print("=== REPORT ===")
    print(f"you started work at: {age}yo")
    print(f"your experience: {experience} years")
    print(f" you start work at: {start_age} yo")

print_report(age, experience, start_age)