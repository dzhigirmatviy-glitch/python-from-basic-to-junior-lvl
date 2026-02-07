import json
def main_training_data():
    data = []
    days = int(input("How many days: "))
    for day in range(1, days + 1):
        while True:
            try:
                minutes = float(input("how many minutes you trained: "))
                data.append({"day": day,
                             "minutes": minutes
                             })
                break
            except ValueError:
                print("please set valid number!")
    return data

def save_training_data(training_data):
    with open("training_data.json", "w", encoding="utf-8") as f:
        json.dump(training_data, f, indent=4, ensure_ascii=False)

def load_training_data():
    try:
        with open("training_data.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print("training_data.json not found")
        return []

if __name__ == "__main__":
    training_data = main_training_data()
    saving = save_training_data(training_data)
    loading = load_training_data()