import random
origonal = ["*","*","*","*"]
        # """sets up the number to be guessed and places it in the list _piles"""
guess = [1, 2, 3, 4]
numbers = []
for i in range(4):#give 4 random numbers, from 1-20
            numbers.append(random.randint(0, 9))

print(f"{numbers[0]} {numbers[1]} {numbers[2]} {numbers[3]}")
for i in numbers:
    for n in guess:
        if i == n:
            origonal[numbers.index(n)] = "O"
        
            

            



        #print(f"{i}{n}") 

print(origonal)
# new = []
# word = 1245
# new = list(str(word))

# print(new)