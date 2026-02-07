import pytest
from bug_hunter import calculate_tips

def test_no_tips():
    total_bill, total_tips, total_splited = calculate_tips(500, None)
    assert total_bill == 500
    assert total_tips == 0
    assert total_splited == 500

def test_5_tips():
    total_bill, total_tips, total_splited = calculate_tips(500, "poor")
    assert total_bill == 525
    assert total_tips == 25
    assert total_splited == 525

def test_2_split_10_tips():
    total_bill, total_tips, total_splited = calculate_tips(500, "good", 2)
    assert total_bill == 550
    assert total_tips == 50
    assert total_splited == 275