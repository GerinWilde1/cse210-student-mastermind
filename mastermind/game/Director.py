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
            player = Player(name)
            self._roster.add_player(player)


    def _get_inputs(self):
        board = self._board.to_string()
        self._console.write(board)
        player = self._roster.get_current()
        self._console.write(f"{player.get_name()}'s turn")
        number = self._console.read_number("What number do you guess(0-9)?")
        location = self._console.read_number(f"Where do you think {number} is?")
        move = Move(number, location)
        Player.set_move(move)

    def _do_updates(self):
        """Updates the important game information for each round of play. In 
        this case, that means updating the board with the current move.

        Args:
            self (Director): An instance of Director.
        """
        player = self._roster.get_current()
        move = player.get_move()
        self._board.apply(move)


    def _do_outputs(self):
        """Outputs the important game information for each round of play. In 
        this case, that means checking if there are stones left and declaring the winner.

        Args:
            self (Director): An instance of Director.
        """
        if self._board.is_empty():
            winner = self._roster.get_current()
            name = winner.get_name()
            print(f"\n{name} won!")
            self._keep_playing = False
        self._roster.next_player()