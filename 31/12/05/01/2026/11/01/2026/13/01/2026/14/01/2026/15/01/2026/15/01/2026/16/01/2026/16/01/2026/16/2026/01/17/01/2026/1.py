import json
def collect_data():
    data = []
    numbers = int(input("how many strings: "))
    for number in range(1, numbers + 1):
        while True:
            try:
                string = input("set your words: ")
                data.append({"number": number,
                             "string": string
                             })
                break
            except ValueError:
                print("please enter a valid number")
    return data

information = collect_data()

def data_selection(information):
    len_string = 5
    for string in information:
        if len(string) > len_string:
            len_string = string
    return len_string

data_selection(information)



