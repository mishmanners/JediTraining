# Have been testing this file to get the functions working... currently still does not print results to the console.

# write a function to generate a sequence of 10 random numbers between 1 and 10

import random

# generate a sequence of random numbers between 1 and 10
def generate_random_number():
    return random.randint(1, 10)
    # print the sequence to the console
    print("Random sequence: " + str(generate_random_number))
                                    
# once we have the random sequence, multiply even numbers by 2, and add 5 to odd numbers
def change_numbers(random_number):
    if random_number % 2 == 0:
        return random_number * 2
    else:
        return random_number + 5
        # print the result
        print("Changed sequence: " + str(numbers))

# now replace any numbers greater than 10 with a 1
def replace_numbers(random_number):
    if random_number > 10:
        return 1
    else:
        return random_number

# print the final sequence to the console
def print_final_sequence(random_number):
    print("Your Jedi mind trick is number: " + str(random_number))

def main():
    random_number = generate_random_number()
    random_number = change_numbers(random_number)
    random_number = replace_numbers(random_number)
    print_final_sequence(random_number)

# uncomment the line to debug the code
print ("My Jedi Mind Tricks are not working")
