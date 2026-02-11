def shift_day_data():
    data = []
    shifts = int(input("How many shifts: "))
    for shift in range(1, shifts + 1):
        print(f"--- Shift {shift} ---")
        hour = int(input("hours worked: "))
        salary = int(input("hourly rate ($): "))
        data.append([shift, hour, salary])
    return data

shift_data = shift_day_data()

def salary_shift(shift_data):
    result = []
    for shift, hour, salary in shift_data:
        regular_pay = min(hour, 8) * salary
        result.append(regular_pay)
    return result

base_salary = salary_shift(shift_data)

def over_time(shift_data):
    result = []
    for shift, hour, salary in shift_data:
        overtime_hours = hour - 8
        if overtime_hours < 0:
            overtime_hours = 0
        overtime_pay = overtime_hours * salary
        result.append((overtime_hours, overtime_pay))
    return result


over_work_shift = over_time(shift_data)


def print_report(shift_data, base_salary, over_work_shift):
    for i, (shift, hour, salary) in enumerate(shift_data):
        overtime_hours, overtime_pay = over_work_shift[i]
        print(f"\nShift {shift}: ")
        print(f"Hours: {hour}, Rate: ${salary}/hour")
        print(f"Regular pay: ${base_salary[i]}")
        print(f"Overtime hours ({overtime_hours}h), overtime_pay: ${overtime_pay}: ")
        print(f" Total salary: ${sum(base_salary) + overtime_pay} ")
print_report(shift_data, base_salary, over_work_shift)
