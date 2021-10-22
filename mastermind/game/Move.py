class Move:
    """A maneuver in the game. The responsibility of Move is to operate and keep track of the players moves.
    
    Stereotype: 
        Information Holder

    Attributes:
        _guess - This is the number guessed by the user. 
    """
    def __init__(self, number, location):
        """The class constructor.
        
        Args:
            self (Board): an instance of Board.
        """
        self._number = number
        self._location = location
        

    def get_number(self):
        """This will return the guess.

        Args:
            self (Move): an instance of Move.
        """
        return self._number

        #location
    def get_location(self):
        """This will return the location.

        Args:
            self (Move): an instance of Move.
        """
        return self._location 