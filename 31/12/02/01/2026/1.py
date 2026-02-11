def welcome_passenger(passenger_name, flight_number):
    print(f"\n passenger name: {passenger_name}")
    print(f"flight Number: {flight_number}")
    print("Happy flight")

def check_documents(passenger_name, passport_valid):
    print(f"passenger name: {passenger_name}")
    if passport_valid == True:
        print(f"passport validation: yes")
    else:
        print(f"passport validation: no")

def assign_seat(passenger_name, seat_number):
    print(f"\npassenger name: {passenger_name}")
    print(f"seat number: {seat_number}")

welcome_passenger("Maria", "FX1795")
check_documents("Maria", True)
assign_seat("Maria", "20F")
print("\n" + "=" * 30 + "\n")
welcome_passenger("Antony", "VY6106")
check_documents("James", False)
assign_seat("James", "3A")