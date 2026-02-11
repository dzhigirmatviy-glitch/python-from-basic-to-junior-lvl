days = int(input("how many days: "))
def get_daily_data(days):
    data = []
    for day in range(1, days + 1):
        print(f"\nday {day}: ")
        tasks = int(input(f"how many task did you had: "))
        hours = int(input(f"how many hours did you work: "))
        difficulty = int(input(f"how difficult it was(1/10): "))
        data.append((tasks, hours, difficulty))
    return data

daily_data = get_daily_data(days)

def calculate_productivity(data):
    efficiencies = []
    for tasks, hours, difficulty in data:
        efficiency = (tasks / hours)
        efficiencies.append(efficiency)
    return efficiencies

my_productivity = calculate_productivity(daily_data)

def main_programm(data):
    efficiencies = calculate_productivity(data)
    for day, ((tasks, hours, difficulty), efficiency) in enumerate(zip(data, efficiencies), start=1):
        print(f"\nday {day}: ")
        print(f"tasks: {tasks}")
        print(f"hours: {hours}")
        print(f"difficulty: {difficulty}")
        print(f"efficiency: {efficiency:.2f} tasks/hour")

    print(f"\n=== SUMMARY ===")
    print(f"Average efficiency: {sum(efficiencies) / len(efficiencies):.2f} tasks/hour")

main_programm(my_productivity)