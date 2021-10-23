import random

        # """sets up the number to be guessed and places it in the list _piles"""
guess = [1, 2, 3, 4]
numbers = []
for i in range(4):#give 4 random numbers, from 1-20
            numbers.append(random.randint(0,9))

print(f"{numbers[0]} {numbers[1]} {numbers[2]} {numbers[3]}")
for i in range(len(numbers)):
    for n in range(len(guess)):
        if i == n:
            



        print(f"{i}{n}") 
