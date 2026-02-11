def calculate_shipping(weight_kg, distance_km, priority=False, fragile=False):
    if weight_kg > 50:
        raise ValueError("Weight kg must be lower than 50")
    if weight_kg >= 1:
        base_cost = 50 + 20 * weight_kg
    else:
        base_cost = 0
    if distance_km > 10:
        distance_cost = (distance_km - 10) * 5
    else:
        distance_cost = 0
    if fragile == True:
        fragile_cost = (base_cost * 50) / 100
    else:
        fragile_cost = 0
    total_base_cost = base_cost + distance_cost + fragile_cost
    if priority == True:
        priority_cost = (total_base_cost * 30) / 100
    else:
        priority_cost = 0
    total_cost = total_base_cost + priority_cost
    if total_cost < 100:
        total_cost = 100
    extras_cost = fragile_cost + priority_cost
    return (round(base_cost, 2),
            round(distance_cost, 2),
            round(extras_cost, 2),
            round(total_cost, 2)
            )
