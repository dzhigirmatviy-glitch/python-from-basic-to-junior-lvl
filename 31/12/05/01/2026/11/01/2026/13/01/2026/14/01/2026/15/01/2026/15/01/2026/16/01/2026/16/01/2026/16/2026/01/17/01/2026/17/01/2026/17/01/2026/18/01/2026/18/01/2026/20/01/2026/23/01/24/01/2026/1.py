import json
def collect_book_data(existing_data):
    data = []
    while True:
        try:
            start_number = existing_data[-1]['id'] + 1 if existing_data else 1
            books = int(input("how many books would you like to add: "))
            for i in range(books):
                id_index = start_number + i
                name = input(f"{id_index}. What`s the name of the book: ")
                readed = False
                data.append({"id": id_index,
                             "name": name,
                             "readed": readed
                             })
            break
        except ValueError:
            print("Please input a correct number!")
        except IndexError:
            return []
    return data

def save_data(all_books):
    with open("all_books.json", "w", encoding="utf-8") as f:
        json.dump(all_books, f, ensure_ascii=False, indent=4)

def load_data():
    while True:
        try:
            with open("all_books.json", "r", encoding="utf-8") as f:
                return json.load(f)
        except FileNotFoundError:
            return []

def show_list_of_books(all_books):
    for data in all_books:
        if data["readed"] == True:
            print(f"{data['id']}. {data['name']} ✅")
        elif data["readed"] == False:
            print(f"{data['id']}. {data['name']} ❌")

def mark_book(all_books):
    show_list_of_books(all_books)
    try:
        select_index = int(input("Select the number of book to mark: "))
    except ValueError:
        print("Please input a correct number!")
        return
    for data in all_books:
        if data["id"] == select_index:
            read_index = input("did you read the book? y/n:" ).lower().strip()
            if read_index == "y":
                data["readed"] = True
            elif read_index == "n":
                data["readed"] = False
            return


def delete_book(all_books):
    show_list_of_books(all_books)
    selection = int(input("Which book would you like to delete: "))
    all_books[:] = [name for name in all_books if name["id"] != selection]
    save_data(all_books)

def main():
    loaded_data = load_data()
    while True:
        try:
            print("=== YOUR BOOK MANAGER ===")
            print("\n1. Add a new book")
            print("2. Show list of the books")
            print("3. Mark a book as read")
            print("4. Delete a book")
            print("5. Exit")

            choice = int(input("Enter your choice: "))
            if choice == 1:
                all_books = collect_book_data(loaded_data)
                loaded_data.extend(all_books)
                save_data(loaded_data)
                print("Your new books has been added successfully! ✅")
            elif choice == 2:
                show_list_of_books(loaded_data)
            elif choice == 3:
                mark_book(loaded_data)
                save_data(loaded_data)
            elif choice == 4:
                delete_book(loaded_data)
                print("Delete successful!")
            elif choice == 5:
                print("Thank you for your time!")
                break
        except ValueError:
            print("Please input a correct number!")

if __name__ == "__main__":
    main()