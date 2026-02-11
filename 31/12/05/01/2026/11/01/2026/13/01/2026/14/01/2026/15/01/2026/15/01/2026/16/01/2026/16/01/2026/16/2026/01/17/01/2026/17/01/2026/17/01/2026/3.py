import json
def collect_book_data(existing_data):
    data = []
    start_number = existing_data[=1]['id'] + 1 if existing_data[=1]['id'] else 1
    while True:
        try:
            books = int(input("how many books would you like to add: "))
            for i in range(books):
                id_index = start_number + i
                name = input("What`s the name of the book: ")
                readed = False
                data.append({"id": id_index
                             "name": name
                             "readed": readed
                             })
            break
        except ValueError:
            print("Please input a correct number!")
    return data



def mark_book(all_books):
    id_readed = int(input("Select which book you would like to mark: "))
    for data in all_books:
        print(f"{data['name'][id_readed]}")