shift = int(input("how many working shifts did you have: "))

difficulty = 0
incident = 0
difficulty_list = []
max_shift = 0
difficulty_day = 0

for shift in range(1, shift + 1):
    print(f"shift {shift}: ")
    difficulty = int(input("difficulty (1-5): "))
    if not (1 <= difficulty <= 5):
        print("error")
    difficulty_list.append(difficulty)
    if difficulty > difficulty_day:
        difficulty_day = difficulty
        max_shift = shift

    incident_list = input("incident? (yes/no): ")
    if incident_list == "yes":
        incident += 1

print("=== RESULTS ===")
print(f"middle difficulty: {sum(difficulty_list) / len(difficulty_list)}")
print(f"shift with incidents: {incident}")
print(f"the most difficult shift: {max_shift} (score {max(difficulty_list)})")