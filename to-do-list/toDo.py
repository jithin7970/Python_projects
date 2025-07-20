# Our To-Do List Machine!

# This is where we will keep all our to-do items.
# It's like an empty magical box (we call it a 'list' in Python).
my_todo_list = []

# --- Helper Functions (like little helpers for our machine) ---

# This helper shows you everything on your to-do list.
def show_list():
    print("\n--- Your To-Do List ---") # Prints a nice title
    if not my_todo_list: # Checks if the list is empty (no items yet)
        print("You don't have anything to do right now! Yay!")
    else:
        # We go through each item in our list, one by one.
        # 'item_number' starts from 1, and 'task' is the actual thing to do.
        for item_number, task in enumerate(my_todo_list, 1):
            print(f"{item_number}. {task}") # Prints like "1. Buy milk"
    print("-----------------------\n")

# This helper adds a new thing to your to-do list.
def add_task(task_description):
    my_todo_list.append(task_description) # Puts the new task at the end of our list
    print(f"Added: '{task_description}' to your list!")

# This helper helps you mark a task as done and remove it.
def mark_done(task_number):
    # Remember, computers start counting from 0, but we want to start from 1.
    # So, if you say '1', the computer thinks '0'.
    list_index = task_number - 1

    # We need to make sure the number you typed is actually on our list.
    # Is the number bigger than 0 AND smaller than or equal to how many things are on the list?
    if 0 <= list_index < len(my_todo_list):
        # If it's a good number, we take that task out of the list.
        completed_task = my_todo_list.pop(list_index)
        print(f"Great job! Marked '{completed_task}' as done and removed it!")
    else:
        # If the number is not on our list, we tell you!
        print("Oops! That's not a valid task number. Please check your list.")

# --- Main Part of Our Machine (where we run the show!) ---

def run_todo_machine():
    print("Welcome to your To-Do List Machine!")

    # This loop keeps our machine running until you tell it to stop.
    while True:
        print("\nWhat would you like to do?")
        print("1. Show my to-do list")
        print("2. Add a new task")
        print("3. Mark a task as done")
        print("4. Exit (Stop the machine)")

        # We ask you to type a number.
        choice = input("Enter your choice (1, 2, 3, or 4): ")

        # Now, we check what number you typed and do the right thing!

        if choice == '1':
            show_list() # Call our helper to show the list

        elif choice == '2':
            new_task = input("What do you need to do? ") # Ask what to add
            add_task(new_task) # Call our helper to add the task

        elif choice == '3':
            # We first show the list so you can see the numbers.
            show_list()
            try:
                task_to_do = int(input("Which task number did you finish? ")) # Ask which number to mark done
                mark_done(task_to_do) # Call our helper to mark it done
            except ValueError:
                # If you type letters instead of a number, we tell you!
                print("That's not a number! Please enter a number from your list.")

        elif choice == '4':
            print("Thanks for using the To-Do List Machine! Goodbye!")
            break # This breaks out of the 'while True' loop and stops the machine.

        else:
            # If you type a number that's not 1, 2, 3, or 4, we tell you!
            print("Hmm, I don't understand that choice. Please try again.")

# --- Make the machine start when we run this code! ---
run_todo_machine()