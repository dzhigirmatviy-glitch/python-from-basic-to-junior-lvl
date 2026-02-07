import json
def collect_data():
    data = []
    numbers = int(input("set how many strings: "))
    for number in range(1, numbers + 1):
        while True:
            try:
                string = input("set your string: ")
                data.append({"number": number,
                             "string": string
                             })
                break
            except ValueError:
                print("please enter a valid number!")
    return data

def evaluate_strings(information):
    delete_count = 0
    for string in information:
        if len(str(string["string"])) > 5:
            try:
                int(string["string"])
                delete_count += 1
                continue
            except ValueError:
                print(string["string"])
        else:
            delete_count += 1
    print(f" deleted count: {delete_count}")
    return delete_count

def save_data(information):
    with open("data.json", "w", encoding="utf-8") as f:
        json.dump(information, f, indent=4)

def load_data():
    with open("data.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    return data

def display_data(loaded_data):
    for string in loaded_data:
        print(f"all strings: {string['string']}")

if __name__ == "__main__":
    information = collect_data()
    evaluation = evaluate_strings(information)
    saved_data = save_data(information)
    loaded_data = load_data()
    display_data(loaded_data)