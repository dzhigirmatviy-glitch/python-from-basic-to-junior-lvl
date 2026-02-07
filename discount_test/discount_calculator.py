class Discount:
    def __init__(self, base: int, discount = 0, vip = False):
        self.base = base
        self.discount = discount
        self.vip = vip

def add_discount():
    data = []
    discount = 0
    while True:
        try:
            base = int(input("Enter base price[1-1000]: "))
            if base < 0 or base > 1000:
                raise ValueError
            vip_index = input("Is costumer VIP?[y/n]: ").lower().strip()
            if vip_index == "y":
                vip = True
            elif vip_index == "n":
                vip = False
            else:
                raise ValueError
            if vip == True:
                discount = 15
            elif base > 500:
                discount = 10
            elif base >= 100:
                discount = 5
            data.append(Discount(base, discount, vip))
            break
        except ValueError:
            print("Invalid input. Please enter a valid input")
    return data

add_data = add_discount()

def show_discounts(add_data):
    for item in add_data:
        final_price = item.base - ((item.base * item.discount) / 100)
        if final_price >= 10:
            print(f"Final price ${final_price:.1f}")
        else:
            print(f"Final price should be more than 10")

show_data = show_discounts(add_data)

