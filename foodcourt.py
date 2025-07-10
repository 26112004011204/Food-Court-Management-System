tables = {
    "1": {"status": "Available", "customer": None},
    "2": {"status": "Available", "customer": None},
    "3": {"status": "Available", "customer": None},
    "4": {"status": "Available", "customer": None},
}

orders = {}
feedback = None



def display_menu():
    import menu_items
    print("\nMenu:")
    for item, price in menu_items.menu_items.items():
        print(f"{item}. {price:.2f}")



def book_table():
    print("\nAvailable Tables:")
    for table, details in tables.items():
        print(f"Table {table}: {details['status']}")
    
    table_number = input("Enter table number to book: ")
    
    if table_number in tables:
        if tables[table_number]["status"] == "Available":
            customer_name = input("Enter your name: ")
            tables[table_number]["status"] = "Occupied"
            tables[table_number]["customer"] = customer_name
            print(f"Table {table_number} has been booked for {customer_name}.")
        else:
            print("Table is not available.")
    else:
        print("Invalid table number.")


def order_food():
    import menu_items
    display_menu()
    table_number = input("Enter your table number: ")
    if table_number in tables and tables[table_number]["status"] == "Occupied":
        while True:
            item = input("Enter item name to order (or 'done' to finish): ")
            if item == "done":
                break
            elif item in menu_items.menu_items:
                quantity = int(input("Enter quantity: "))
                if table_number not in orders:
                    orders[table_number] = {}
                if item in orders[table_number]:
                    orders[table_number][item] += quantity
                else:
                    orders[table_number][item] = quantity
            else:
                print("Invalid item number.")
    else:
        print("Table is not occupied or doesn't exist.")





def save_orders(orders):
    with open("orders.txt", "w") as file:
        for table, items in orders.items():
            file.write(f"Table {table}:\n")
            for item, quantity in items.items():
                file.write(f"{item}: {quantity}\n")

def calculate_bill():
    import menu_items
    table_number = input("Enter table number to generate bill: ")
    if table_number in orders:
        total = 0
        for item, quantity in orders[table_number].items():
            total += menu_items.menu_items[item] * quantity
        print(f"Total Bill for Table {table_number}: ${total:.2f}")
        del orders[table_number]
        tables[table_number]["status"] = "Available"
        tables[table_number]["customer"] = None
    else:
        print("No orders found for the table.")






def give_feedback():
    global feedback
    feedback = input("Enter your feedback: ")
    print("Thank you for your feedback!")

    


def display_feedback():
    if feedback:
        print(f"\nFeedback: {feedback}")
    else:
        print("\nNo feedback given yet.")

        

def run():
    while True:
        print("\nFood Court Management System")
        print("1. Display Menu")
        print("2. Book Table")
        print("3. Order Food")
        print("4. Calculate Bill")
        print("5. Give Feedback")
        print("6. Display Feedback")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            display_menu()
        elif choice == "2":
            book_table()
        elif choice == "3":
            order_food()
        
        elif choice == "4":
            calculate_bill()
        elif choice == "5":
            give_feedback()
        elif choice == "6":
            display_feedback()
        elif choice == "7":
            print("Thank you for using our system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")




i=1
while(i>0):
    run()
    i-=1
