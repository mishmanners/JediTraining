# write a function to generate a sequence of 10 random numbers between 1 and 10

import random

# generate a sequence of 10 random numbers between 1 and 10 and print the result
numbers = [random.randint(1, 10) for i in range(10)]
print("Original sequence: " + str(numbers))

# once we have the sequence (numbers), multiply even numbers by 2, and add 5 to odd numbers
for i in range(len(numbers)):
    if numbers[i] % 2 == 0:
        numbers[i] = numbers[i] * 2
    else:
        numbers[i] = numbers[i] + 5
        #print the result
print("Changed sequence: " + str(numbers))

# if a number in the new sequence is great than 10, relace it with a 1
for i in range(len(numbers)):
    if numbers[i] > 10:
        numbers[i] = 1

# print the final new sequence to the console
print("Your Jedi mind trick is number: " + str(numbers))