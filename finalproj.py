if __name__ == "__main__":
    print("Welcome to the Restaurant Menu")
    print("Menu:")
    menu = {
        1: ("Hamburger", 8.99),
        2: ("Spaghetti and Meatballs", 12.99),
        3: ("French Fries", 6.99),
        4: ("Chicken Sandwich", 8.99),
        5: ("Quesadilla", 10.99),
        6: ("Cheese Pizza", 9.99),
        7: ("Pepperoni Pizza", 10.99)
    }
    selected_items = []
#this first piece of code is just the menu and the prices associated with each item
    while True:
        choice = input("Enter item number: ")
        if choice.lower() == 'done':
            break
        elif choice.isdigit() and int(choice) in menu:
            selected_items.append(int(choice))
        else:
            print("Please enter a valid number")
#this code handles the input and associates the number inputted with the number of the food on the menu
#i learned the break command from google it allows you to exit a loop when a condition is met
    if selected_items:
        print("Your order:")
        total = sum(menu[item][1] for item in selected_items)
        for item in selected_items:
            name, price = menu[item]
            print(f"{item}. {name} - ${price:.2f}")
        print(f"Total: ${total:.2f}")
#here is where the final price of the items purchased is listed