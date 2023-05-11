# write a function to generate a random number between 1 and 10

import random

# generate a random number between 1 and 10
def generate_random_number():
    return random.randint(1, 10)

# once we have the random number, multiply even numbers by 2
def multiply_even_numbers_by_two(random_number):
    if random_number % 2 == 0:
        return random_number * 2
    else:
        return random_number

# once we have the random number, add 5 to odd numbers
def add_five_to_odd_numbers(random_number):
    if random_number % 2 != 0:
        return random_number + 5
    else:
        return random_number

# once we have the random number, replace any number greater than 10 with 1
def replace_numbers_greater_than_ten(random_number):
    if random_number > 10:
        return 1
    else:
        return random_number

# print the final sequence to the console
def print_final_sequence(random_number):
    print("Your Jedi mind trick is number: " + str(random_number))

# main function
def main():
    random_number = generate_random_number()
    random_number = multiply_even_numbers_by_two(random_number)
    random_number = add_five_to_odd_numbers(random_number)
    random_number = replace_numbers_greater_than_ten(random_number)
    print_final_sequence(random_number)