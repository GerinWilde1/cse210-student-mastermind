import random
from game import Player
class Board:


          def __init__(self):
            self._numbers = []
            self._prepare()
          

          def apply(self, move):

            pass
          
          def to_string(self):
            """output that will be used as a visual for the players."""
            text = "\n -------------------------"
            for num, sequence in self._numbers():
              text += f"Player {num}: {sequence[1]}, {sequence[2]}\n"
            text += "\n-------------------------"
    
          
          def _prepare(self):

            """sets up the number to be guessed and places it in the list _numbers"""
            for i in range(4):
              self._numbers.append(random.randint(0-9))
            
            
          
            