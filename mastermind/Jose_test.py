# import random
# def _prepare():
#         # """sets up the number to be guessed and places it in the list _piles"""
        
#         numbers = []
#         for i in range(4):#give 4 random numbers, from 1-20
#                     numbers.append(random.randint(0,9))
#         return numbers
# print(_prepare)


def to_string(self):

        text =  "\n--------------------"
        for pile, stones in enumerate(self._piles):
                text += (f"\n{pile}: " + "O " * stones)
        text += "\n--------------------"
        return text
print(to_string)