days = int(input(f"How many worker days: "))

passengers = []
flights = []
delayeds = 0
clears = 0
effectives = []
max_effectives = 0
best_day = 0

for day in range(1, days + 1):
    print(f"day: {day}")
    passenger = int(input(f"passengers: "))
    passengers.append(passenger)

    flight = int(input(f"flights: "))
    flights.append(flight)

    effective = passenger / flight
    effectives.append(effective)
    if effective > max_effectives:
        max_effectives = effective
        best_day = day

    delayed = input("dalayed? (yes/no): ")
    if delayed == "yes":
        delayeds += 1
    else:
        clears += 1

mid_passengers = sum(passengers) / sum(flights)

print("=== RESULTS ===")
print(f"All passengers: {sum(passengers)}")
print(f"middle passengers for flight: {mid_passengers:.1f} pass/flight")
print(f"days with delayeds: {delayeds}, without delayeds: {clears}")
print(f"the most effeciency day: {best_day} ({max_effectives} pass/flight) ")