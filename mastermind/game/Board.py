import random

class Board:


          def __init__(self):
                    self._numbers = []
                    self._prepare()


          def apply(self, move):
                    number = move.get_number()
          def is_empty(self):
                    """may not be needed"""
                    
                    pass
                    
          def to_string(self):
                    """output that will be used as a visual for the players."""
                    pass
          def _prepare(self):
                    """sets up the number to be guessed and places it in the list _numbers"""

                    