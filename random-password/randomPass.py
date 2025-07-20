# Our Super Password Maker!

# First, we need some special tools from Python.
# 'random' helps us pick things by chance, like drawing names from a hat.
# 'string' helps us get all the letters (big and small), numbers, and symbols easily.
import random
import string

# --- Helper Function (our password-making helper) ---

def generate_strong_password(length):
    # This is like a big box full of all the characters we can use in a password.
    # It has:
    # 1. Lowercase letters (a, b, c...)
    # 2. Uppercase letters (A, B, C...)
    # 3. Numbers (0, 1, 2...)
    # 4. Special symbols (!, @, #, $...)
    all_characters = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation

    # We need to make sure the password is at least a little bit long to be strong.
    # If someone asks for a password shorter than 8, we'll make it 8 anyway.
    if length < 8:
        print("A super strong password should be at least 8 characters long.")
        print("Making your password 8 characters long instead.")
        length = 8 # We make sure it's at least 8

    # Now, let's make sure our password has at least one of each type of character,
    # so it's extra strong!
    # We pick one lowercase, one uppercase, one number, and one symbol.
    password = [
        random.choice(string.ascii_lowercase), # A random small letter
        random.choice(string.ascii_uppercase), # A random BIG letter
        random.choice(string.digits),          # A random number
        random.choice(string.punctuation)      # A random symbol
    ]

    # Now, we fill up the rest of the password length with any random characters
    # from our big box, until we reach the desired length.
    # We already have 4 characters, so we need 'length - 4' more.
    for _ in range(length - 4): # The '_' is just a placeholder because we don't need a counter here.
        password.append(random.choice(all_characters))

    # Finally, we shuffle all the characters in our password list.
    # This is like shaking the hat so the order is super random and hard to guess!
    random.shuffle(password)

    # We join all the characters together to make one long password word.
    return "".join(password)

# --- Main Part of Our Machine (where we run the show!) ---

def run_password_maker():
    print("Welcome to your Super Password Maker!")
    print("This machine will help you create strong and random passwords!")

    # This loop keeps our machine running until you tell it to stop.
    while True:
        try:
            # We ask you how long you want your password to be.
            # We use 'int()' because we expect a whole number.
            desired_length = int(input("How long should your password be (e.g., 12)? Or type 0 to Exit: "))

            if desired_length == 0:
                print("Thanks for using the Super Password Maker! Goodbye!")
                break # This stops our machine.
            elif desired_length < 0:
                print("Password length cannot be a negative number. Please try again.")
                continue # Go back to the start of the loop

            # Call our helper to make the password!
            new_password = generate_strong_password(desired_length)

            print("\n--- Your New Super Strong Password ---")
            print(f"Password: {new_password}")
            print("--------------------------------------\n")
            print("Remember to keep your passwords safe and secret!")

        except ValueError:
            # If you type letters instead of a number, we tell you!
            print("Oops! That's not a valid number. Please enter a whole number for the length.")
        except Exception as e: # Catch any other unexpected errors
            print(f"An unexpected error happened: {e}")

# --- Make the machine start when we run this code! ---
run_password_maker()