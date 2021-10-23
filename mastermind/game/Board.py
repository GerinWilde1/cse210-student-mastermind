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
            
            
            name = Player.get_name()
            code = str(random.randint(1000, 9999))
    
        
            self._items[player] = [code] 
            self._items[player] = [code]

            def get_current(self):
                pass    
            