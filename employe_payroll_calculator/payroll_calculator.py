def calculate_salary(hours_worked, hourly_rate, overtime_hours=0, bonus_percent=0):
    if hours_worked is None:
        hours_worked = 0
    if hourly_rate is None:
        hourly_rate = 0
    if overtime_hours is None:
        overtime_hours = 0
    if bonus_percent is None:
        bonus_percent = 0
    base_salary = hours_worked * hourly_rate
    overtime_salary = overtime_hours * hourly_rate * 1.5
    bonus_amount = ((base_salary + overtime_salary) * bonus_percent) / 100
    gross_salary = base_salary + overtime_salary + bonus_amount
    tax_amount = ((gross_salary) * 19) / 100
    net_salary = gross_salary - tax_amount
    if net_salary < 500:
        net_salary = 500
    return (round(gross_salary, 2),
            round(tax_amount, 2),
            round(net_salary, 2),
            round(bonus_amount, 2)
            )

