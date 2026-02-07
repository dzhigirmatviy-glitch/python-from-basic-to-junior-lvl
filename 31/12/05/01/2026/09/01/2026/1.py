def get_user_data():
    while True:
        try:
            weight = float(input("set your weight: "))
            height = float(input("set your height in (meters): "))
            return weight, height
        except ValueError:
            print("Please enter a valid number")
weight, height = get_user_data()

def calculate_bmi(weight, height):
    return weight / (height ** 2)

bmi = calculate_bmi(weight, height)

def get_bmi_category(bmi):
    if bmi < 18.5:
        return "underweight"
    elif bmi < 25:
        return "normal weight"
    elif bmi < 30:
        return "overweight"
    else:
        return "obese"

bmi_category = get_bmi_category(bmi)

def print_bmi_report(weight, height, bmi, bmi_category):
    print("=== BMI REPORT ===")
    print(f"\nyour weight: {weight} kg")
    print(f"your height: {height} m")
    print(f"your bmi:{bmi:.1f}, your category: {bmi_category}")
    print("End of the report...")

print_bmi_report(weight, height, bmi, bmi_category)