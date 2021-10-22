import random

        # """sets up the number to be guessed and places it in the list _piles"""
        
numbers = []
for i in range(4):#give 4 random numbers, from 1-20
            numbers.append(random.randint(0,9))

print(f"{numbers[0]} {numbers[1]} {numbers[2]} {numbers[3]}")