import json
def add_operations(existing_operations):
    data = []
    start_number = existing_operations[-1]['id'] + 1 if existing_operations else 1
    days = int(input("How many days would you like to add: "))
    for i in range(days):
        while True:
            try:
                id_code = start_number + i
                date = input("set your date: ")
                category = input("set your category: ")
                amount = float(input("set your expenses or income: "))
                description = input("set description of your financial operations: ")
                data.append({"id": id_code,
                             "date": date,
                             "category": category,
                             "amount": amount,
                             "description": description
                })
                break
            except ValueError:
                print("Please enter a value number!")
    return data

def show_all_operations(all_operations):
    for data in all_operations:
        print(f"{data['id']}. {data['date']} | {data['category']} | {data['amount']} | {data['description']}")

def save_financial_data(all_operations):
    with open("financial_data.json", "w", encoding="utf-8") as f:
        json.dump(all_operations, f, ensure_ascii=False, indent=4)

def load_financial_data():
    try:
        with open("financial_data.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def current_balance(all_operations):
    current_balance = 0
    for data in all_operations:
        current_balance += data["amount"]
    return current_balance

def statistic_by_category(all_operations):
    operation_sum = {}
    for data in all_operations:
        category = data['category']
        if category not in operation_sum:
            operation_sum[category] = 0
        operation_sum[category] += data["amount"]
    return operation_sum


all_operations = load_financial_data()
def main():
    while True:
        try:
            print("=== FINANCE TRACKER ===")
            print("\n1. Show all operations")
            print("2. Add new operation")
            print("3. Show statistics by category")
            print("4. Show current balance")
            print("5. Exit")
            choose = int(input("\nPlease choose a number [1-5]: "))
            if choose == 1:
               show_all_operations(all_operations)
            elif choose == 2:
                new_operations = add_operations(all_operations)
                all_operations.extend(new_operations)
                save_financial_data(all_operations)
            elif choose == 3:
                for category, amount in statistic_by_category(all_operations).items():
                    print(f"{category}: ${amount}")
            elif choose == 4:
                print(f"${current_balance(all_operations)}")
            elif choose == 5:
                break
        except ValueError:
            print("Please set valid number!!!")

if __name__ == "__main__":
    main()