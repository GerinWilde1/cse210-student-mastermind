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
        """"""
        
        
        self._prepare_game()
        while self._keep_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs

    def _prepare_game(self):


        for n in range(2):
            name = self._console.read(f"Please enter a name for player {n + 1}: ")
            player = player(name)
            self._roster.add_player(player)


    def _get_inputs(self):
        """This gets the inputs from the player each round and assigns them where they need to go.
        
        """
        
        board = self._board.to_string() #gets the players display from the board class
        self._console.write(board) #outputs on th escreen the information it gets from "board"
        player = self._roster.get_current() #gets the current players information
        self._console.write(f"{player.get_name()}'s turn") #alerts the player that it's their turn
        number = self._console.read_number("What number do you guess(0-9)?") #asks the player what their guess is
        location = self._console.read_number(f"Where do you think {number} is?") # asks the location that the player thinks their guess is in
        move = Move(number, location) #passes number and location to the Move class so they can be processed
        player.set_move(move) #Changes the move variable in Player from None to the numbers that it should be 

    def _do_updates(self):
        """Updates the important game information for each round of play. In 
        this case, that means updating the board with the current move.

        Args:
            self (Director): An instance of Director.
        """
        player = self._roster.get_current() # gets the current player from the roster
        move = player.get_move()
        self._board.apply(move)


    def _do_outputs(self):
        """Outputs the important game information for each round of play. In 
        this case, that means checking if there are stones left and declaring the winner.

        Args:
            self (Director): An instance of Director.
        """
        if self._board.is_solved():
            winner = self._roster.get_current()
            name = winner.get_name()
            print(f"\n{name} won!")
            self._keep_playing = False
        self._roster.next_player()