from discount_calculator import Discount
def test_discount_creation():
    base = 750
    discount = 10
    vip = False

    d = Discount(base, discount, vip)

    assert d.base == base
    assert d.discount == discount
    assert d.vip == vip

def test_discount():
    d = Discount(750, 10, False)

    final_price = d.base - ((d.base * d.discount) / 100)

    assert d.base == 750
    assert d.discount == 10
    assert d.vip == False
    assert final_price == 675