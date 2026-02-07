import pytest
from payroll_calculator import calculate_salary

def test_base_salary():
    gross_salary, tax_amount, net_salary, bonus_amount = calculate_salary(100, 10, None, None)
    assert gross_salary == 1000
    assert tax_amount == 190
    assert net_salary == 810
    assert bonus_amount == 0
def test_overtime_salary():
    gross_salary, tax_amount, net_salary, bonus_amount = calculate_salary(120, 12, 2, None)
    assert gross_salary == 1476
    assert tax_amount == 280.44
    assert net_salary == 1195.56
    assert bonus_amount == 0
def test_bonus_amount():
    gross_salary, tax_amount, net_salary, bonus_amount = calculate_salary(135, 13, 25, 10)
    assert gross_salary == 2466.75
    assert tax_amount == 468.68
    assert net_salary == 1998.07
    assert bonus_amount == 224.25
def test_minimun_wage():
    gross_salary, tax_amount, net_salary, bonus_amount = calculate_salary(19, 10, 2, 3)
    assert gross_salary == 226.6
    assert tax_amount == 43.05
    assert net_salary == 500
    assert bonus_amount == 6.6

    """base_salary = hours_worked * hourly_rate
    overtime_salary = overtime_hours * hourly_rate * 1.5
    bonus_amount = ((base_salary + overtime_salary) * bonus_percent) / 100
    gross_salary = base_salary + overtime_salary + bonus_amount
    tax_amount = ((gross_salary) * 19) / 100
    net_salary = gross_salary - tax_amount"""
