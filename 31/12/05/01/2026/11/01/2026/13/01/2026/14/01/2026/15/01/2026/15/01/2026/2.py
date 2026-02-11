import json
def get_reading_data():
    days = int(input("how many days: "))
    data = []
    for day in range(1, days + 1):
        while True:
            try:
                hours = float(input("how many hours: "))
                data.append({"day": day,
                            "hours": hours
                             })
                break
            except ValueError:
                print("please enter a value number")
    return data

def save_reading_data(reading_data):
    with open("readingData.json", "w", encoding="utf-8") as f:
        json.dump(reading_data, f, indent=4, ensure_ascii=False)

if __name__ == "__main__":
    reading_data = get_reading_data()
    saving = save_reading_data(reading_data)