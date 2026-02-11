from shipping_calculator import calculate_shipping
import pytest
def test_base_calculator():
    base_cost, distance_cost, extras_cost, total_cost = calculate_shipping(30, 40, False, False)
    assert base_cost == 650
    assert distance_cost == 150
    assert extras_cost == 0
    assert total_cost == 800
def test_priority_included():
    base_cost, distance_cost, extras_cost, total_cost = calculate_shipping(20, 50, True, False)
    assert base_cost == 450
    assert distance_cost == 200
    assert extras_cost == 195
    assert total_cost == 845
def test_fragile_included():
    base_cost, distance_cost, extras_cost, total_cost = calculate_shipping(20, 50, True, True)
    assert base_cost == 450
    assert distance_cost == 200
    assert extras_cost == 487.5
    assert total_cost == 1137.5
def test_min_price():
    base_cost, distance_cost, extras_cost, total_cost = calculate_shipping(2, 5, False, False)
    assert base_cost == 90
    assert distance_cost == 0
    assert extras_cost == 0
    assert total_cost == 100
def test_max_weight():
    with pytest.raises(ValueError):
        calculate_shipping(100, 5, False, False)

