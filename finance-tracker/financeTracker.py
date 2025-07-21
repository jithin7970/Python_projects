# This program helps you keep track of your money!

# We need a place to store all the money you have, and all the money you spend.
# Think of it like a special box where we put numbers.
# We'll use a "list" to hold our transactions. A list is like a shopping list, but for numbers!
transactions = []

def add_income(amount):
    # This function is like putting money INTO your box.
    # We'll add a positive number because you got more money.
    transactions.append(amount)
    print(f"Great! You added ${amount} to your money.")

def add_expense(amount):
    # This function is like taking money OUT of your box.
    # We'll add a negative number because money went away.
    transactions.append(-amount) # We use a minus sign to show it's an expense
    print(f"Oops! You spent ${amount}.")

def show_balance():
    # This function helps us see how much money is left in your box.
    # We'll add up all the numbers in our "transactions" list.
    total_money = sum(transactions) # 'sum' means adding all the numbers together
    print("---")
    print(f"Your total money right now is: ${total_money}")
    print("---")

def show_transactions():
    # This function shows you all the times you put money in or took money out.
    print("\n--- Your Money History ---")
    if not transactions: # This checks if the list is empty (no money story yet!)
        print("You haven't added any money or expenses yet.")
    else:
        for transaction in transactions: # We go through each number in our list
            if transaction > 0: # If the number is positive, it was money you got
                print(f"Got: ${transaction}")
            else: # If the number is negative, it was money you spent
                print(f"Spent: ${abs(transaction)}") # 'abs' makes the negative number positive so it looks nice
    print("------------------------")

# Now, let's make a menu so you can tell the computer what you want to do!
while True: # This loop keeps the menu going until you say "stop"
    print("\nWhat do you want to do with your money?")
    print("1. Add money (Income)")
    print("2. Spend money (Expense)")
    print("3. See how much money you have (Balance)")
    print("4. See all your money movements (Transactions)")
    print("5. Stop this program")
    choice = input("Type the number of your choice: ") # We ask you to type a number

    if choice == '1':
        # If you choose 1, we ask how much money you got
        try: # 'try' helps us catch mistakes, like if you type "apple" instead of a number
            amount = float(input("How much money did you get? $")) # 'float' means it can have decimal points, like $5.50
            if amount > 0:
                add_income(amount)
            else:
                print("Please enter a positive amount.")
        except ValueError: # If there's a mistake, we tell you!
            print("That's not a valid number. Please try again with a number like 10 or 5.50.")
    elif choice == '2':
        # If you choose 2, we ask how much money you spent
        try:
            amount = float(input("How much money did you spend? $"))
            if amount > 0:
                add_expense(amount)
            else:
                print("Please enter a positive amount.")
        except ValueError:
            print("That's not a valid number. Please try again with a number like 10 or 5.50.")
    elif choice == '3':
        # If you choose 3, we show your balance
        show_balance()
    elif choice == '4':
        # If you choose 4, we show all your transactions
        show_transactions()
    elif choice == '5':
        # If you choose 5, we say goodbye and stop the program
        print("Thanks for tracking your money! Goodbye!")
        break # This breaks out of the 'while True' loop and stops the program
    else:
        # If you type something else, we tell you to pick a number from the list
        print("Oops! Please pick a number from 1 to 5.")