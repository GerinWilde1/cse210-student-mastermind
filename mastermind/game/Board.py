import random
from typing import Text
class Board:


  def __init__(self):
    self._numbers = []
    self._prepare()
    self.origional = ["*","*","*","*"]
  

  def apply(self, move):
    for i in self._numbers:
      for n in move._guess:
        if i == n and move._guess.index(n) != self._numbers.index(i):
            self.origonal[move.guess.index(n)] = "O"
        elif i == n:
            self.origonal[self._numbers.index(n)] = "X"

    
  
  def to_string(self):
    """output that will be used as a visual for the players."""
    text = "\n -------------------------"
    for num, sequence in self._numbers():
      text += f"Player {num}: {sequence[1]}, {sequence[2]}\n"
    text += "\n-------------------------"

  
  def _prepare(self):

    """sets up the number to be guessed and places it in the list _numbers"""
    for i in range(4):
      self._numbers.append(random.randint(0, 9))
            
            
          
            