import random

class Board:


    def __init__(self):
        self._numbers = []
        self._prepare()


    def apply(self, move):
        number = move.get_numbers()
        location = move.get_location()
        self._piles[pile] = max(0, self._piles[number] - colors)
    
    
    def is_solved(self):
            
            
            pass
            
    def to_string(self):
        text = "\n-------------------------\n"
        for pile, colors in enumerate(self._numbers):
                    text += (f"\n{pile}: " + "O " * colors)
        text += "-------------------------\n"
        return text  



    def _prepare(self):
        # """sets up the number to be guessed and places it in the list _piles"""
        
        numbers = []
        for i in range(4):#give 4 random numbers, from 1-20
                    self._numbers.append(random.randint(0,9))
        return numbers