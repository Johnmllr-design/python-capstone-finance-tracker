# this is a python script for a simple finance tracker tha tis the capstone of my externship 
# at Cognizant.

# print  a welcome message
print("Welcome to the Personal Finance Tracker!")


# declare a dictionary as the underlying data structure to store transactions
transactions = {}


# functions to handle user given data:
def add_expense():
    # get the expense details from the user
    category = input("Enter the category of the expense: ")
    description = input("Enter a description of the expense: ")
    amount = float(input("Enter the amount of the expense: "))

    if category in transactions:
        transactions[category].append((description, amount))
    
    else:
        transactions[category] = [(description, amount)]


# print the total for each category
def view_summary():
    print("Summary:")
    for category in transactions:
        total = 0
        for expense in transactions[category]:
            for description, amount in expense:
                total += amount
        print(category + " : " + "$" + str(total))


# print the categories and their respective expenses
def view_expenses():
    print("Expenses:")
    for category in transactions:
        print(category)
        for expense in transactions[category]:
            print(expense)



# use a loop to repeatedly ask the user for input
option = -1
while option != 4:
    try:
        print("What would you like to do?")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Summary")
        print("4. Exit")
        option = int(input("Choose an option: "))

        if option >= 1 and option <= 4:
            if option == 1:
                add_expense()
            elif option == 2:
                view_expenses()
            elif option == 3:
                view_summary()
            elif option == 4:
                print("Thank you for using your Personal Finance Tracker. Goodbye!")
                break
        else:
            print("Invalid option. Please choose a number between 1 and 4.")
            continue

    except ValueError:
        print("Invalid input. Please enter a number.")
        continue





        


    