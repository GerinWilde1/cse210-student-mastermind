import random

import random

empty = ["*","*","*","*",]
guess_test = ["1", "2", "3", "4"]
user_list = []
numbers = []
for i in range(4):#give 4 random numbers, from 1-20
            numbers.append(random.randint(0,9))

guess1 =input("please enter a number from 1-4")

digit_string = str(guess1)
digit_map = map(int, digit_string)
digit_list = list(digit_map)
print(digit_list)
print(numbers)

# index = guess_test.index(guess1)
# print(index)

# empty[index] = "X"
# print(empty) 












# original = ["1","2","3","4"]
# print(original)
# new_boards = ["O","O","O","O"]
# print(new_boards)
# # def random_sample ():
# #     n=random.sample(range(1,20), 4)
# #     return n
# # print(random_sample())
# guess1 = input("please enter the number: ")
# guess2 = input("please enter the number: ")
# guess3 = input("please enter the number: ")
# guess4 = input("please enter the number: ")




# if guess1 in original:
#     for string in new_boards:
#         new_string = string.replace("0", guess1)


#         new_boards.append(new_string)

# print(new_boards)

# original = ["*","*","*","*",]
# guess = [1, 2, 3, 4]

# numbers = []
# for i in range(4):#give 4 random numbers, from 1-20
#             numbers.append(random.randint(0,9))

# print(f"{numbers[0]} {numbers[1]} {numbers[2]} {numbers[3]}")
# for i in numbers:
#     for n in guess:

            
            
            
#         print(f"{i}{n}")
            
