from game.Player import Player
from game.Board import Board
from game.Console import Console
from game.Move import Move
from game.Roster import Roster

class Director:


    def __init__(self):
        self._player = Player()
        self._board = Board()
        self._console = Console()
        self._roster = Roster()
        self._keep_playing = True
        self._move = None



    def start_playing(self):
        """Gets everything going and runs through each function in order to get the game going."""
        
        
        self._prepare_game()
        while self._keep_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()

    def _prepare_game(self):
        """This gets the name of each of the players and adds them to the roster."""

        for n in range(2):#makes sure there are only two players
            name = self._console.read(f"Please enter a name for player {n + 1}: ")#asks for each of the players names
            player = Player(name)#makes the payers information a simple variable
            self._roster.add_player(player)#adds the players name to a list in the roster


    def _get_inputs(self):
        """This gets the inputs from the player each round and assigns them where they need to go. """
        
        board = self._board.to_string() #gets the players display from the board class
        self._console.write(board) #outputs on th escreen the information it gets from "board"
        player = self._roster.get_current() #gets the current players information
        self._console.write(f"{player.get_name()}'s turn") #alerts the player that it's their turn
        number = self._console.read_number("What number do you guess(0-9)?") #asks the player what their guess is
        location = self._console.read_number(f"Where do you think {number} is?") # asks the location that the player thinks their guess is in
        move = Move(number, location) #passes number and location to the Move class so they can be processed
        player.set_move(move) #Changes the move variable in Player from None to the numbers that it should be 

    def _do_updates(self):
        """Updates important information like the move made by the player."""
        
        player = self._roster.get_current() # gets the current player from the roster
        move = player.get_move()
        self._board.apply(move) #this updates the move made by whichever player.


    def _do_outputs(self):
        """depending on if the player won or not it will put out different things. 
        like if they win it will let them know or if they lost to will move to the next player."""
        if self._board.is_solve():
            winner = self._roster.get_current()
            name = winner.get_name()
            print(f"\n{name} won!")
            self._keep_playing = False
        self._roster.next_player()