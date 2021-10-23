import random

original = ["1","2","3","4"]
print(original)
new_boards = ["O","O","O","O"]
print(new_boards)
# def random_sample ():
#     n=random.sample(range(1,20), 4)
#     return n
# print(random_sample())
guess1 = input("please enter the number: ")
# guess2 = input("please enter the number: ")
# guess3 = input("please enter the number: ")
# guess4 = input("please enter the number: ")




if guess1 in original:
    for string in new_boards:
        new_string = string.replace("0", guess1)


        new_boards.append(new_string)

    print(new_boards)