# write a function to generate a sequence of 10 random numbers between 1 and 10

import random

# generate a sequence of 10 random numbers between 1 and 10
def generate_random_number():
    random_number = random.randint(1, 10)
    return random_number
    print("Your sequence is:" + random_number)

# once we have the sequence, multiply all the even numbers by 2, and add 5 to all the odd numbers
def change_numbers(random_number):
    if random_number % 2 == 0:
        random_number = random_number * 2
    else:
        random_number = random_number + 5
    return random_number
    # if the new number is greater than 10, replace it with 1
    if random_number > 10:
        random_number = 1
    return random_number

# print the final new sequence to the console
def print_final_sequence(random_number):
    print("Your Jedi mind trick is number: " + random_number)

# main function to run the code
def main():
    random_number = generate_random_number()
    random_number = change_numbers(random_number)
    print_final_sequence(random_number)

# Uncomment the next line to test the code
print("My Jedi Powers are weak")