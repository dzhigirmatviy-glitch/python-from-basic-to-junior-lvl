import json
def add_habit_day():
    data = []
    while True:
        try:
            days = int(input("Input the number of days: "))
            for day_index in range(days):
                print(f"day {day_index+1}")
                date = input("Input the date of the habit: ")
                numbers = int(input("How many habits would you like to add: "))
                comment = input("Input the comment of the habit: ")
                habits_dict = {}
                for habit_index in range(numbers):
                    habits = input("Input an habits: ")
                    done = input("Do you had this habit today? [y/n]: ")
                    if done == "y":
                        habits_dict[habits] = True
                    else:
                        habits_dict[habits] = False
                data.append({"id": day_index+1,
                          "date": date,
                          "habits": habits_dict,
                          "comment": comment
                })
            break
        except ValueError:
            print("Invalid input of number. Please try again.")
    return data

habit_day = add_habit_day()

def show_all_days(habit_day):
    for habits_dict in habit_day:
        print(f"{habits_dict['date']}: {habits_dict['habits']} *comment: {habits_dict['comment']}*")

show_all_days(habit_day)