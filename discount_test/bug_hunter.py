def calculate_tips(bill_amount, service_quality, split_people = 1):
    service = service_quality.lower().strip()
    if service == "poor":
        tips = 5
    elif service == "good":
        tips = 10
    elif service == "excellent":
        tips = 15
    elif service == None:
        tips = 0
    total_tips = (bill_amount * tips) / 100
    if total_tips < 0 or total_tips > 100:
        raise ValueError
    total_bill = bill_amount + total_tips
    total_splited = total_bill / split_people
    if bill_amount > 1000 or bill_amount < 100:
        raise ValueError
    if split_people <= 0:
        raise ValueError
    elif split_people > 1:
        return round(total_bill, 2), round(total_tips, 2), round(total_splited, 2)
    else:
        return total_bill, total_tips, total_splited
