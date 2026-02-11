def calculate_efficiency(passengers, hours):
    efficiency = passengers / hours
    print(f"efficiency: {efficiency:.1f} pass/hour")
    return efficiency

def evaluate_shift(efficiency):
    if efficiency > 50:
        return "good shift"
    elif efficiency > 30:
        return "normal shift"
    else:
        return "bad shift"

def analyze_work_shift(passenger_name, passengers, hours):
    print(f"\npassenger name: {passenger_name}")
    efficiency = calculate_efficiency(passengers, hours)
    shift = evaluate_shift(efficiency)
    return efficiency, shift


analyze_work_shift("matthew", 450, 5)
analyze_work_shift("Antony", 4500, 5)
