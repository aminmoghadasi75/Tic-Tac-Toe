import random
from typing import List, Union

from colorama import Fore, Style, init
from tabulate import tabulate


class TicTacToe:
    def __init__(self) -> None:
        """
        Initialize the Tic Tac Toe game.
        """
        self.board: List[Union[str, int]] = [i for i in range(1, 10)]
        self.players: List[str] = [Fore.BLUE + 'X' + Style.RESET_ALL, Fore.RED + 'O' + Style.RESET_ALL]
        self.player_turn: str = random.choice(self.players)

    def show_board(self) -> None:
        """
        Display the current game board.
        """
        formatted_board = [self.format_cell(cell) for cell in self.board]
        table = [
            formatted_board[0:3],
            formatted_board[3:6],
            formatted_board[6:9]
        ]
        print(tabulate(table, tablefmt="fancy_grid"))

    def format_cell(self, cell: Union[str, int]) -> str:
        """
        Format the cell with appropriate color and styling.
        """
        if str(cell).isdigit():
            return f'{Fore.WHITE}{cell}{Style.RESET_ALL}'
        return cell

    def check_winner(self) -> bool:
        """
        Check if there is a winner or if the game ended in a draw.
        """
        winning_conditions = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]             # Diagonals
        ]

        for condition in winning_conditions:
            a, b, c = condition
            if self.board[a] == self.board[b] == self.board[c]:
                winner = self.board[a]
                print(f"Player {winner} won the game!")
                return True

        if all(isinstance(cell, str) for cell in self.board):
            print("It's a draw!")
            return True

        return False

    def check_empty(self, loc: int) -> bool:
        """
        Check if the specified location on the board is empty.
        """
        return str(self.board[loc - 1]).isdigit()

    def fill_stage(self, player: str, loc: int) -> None:
        """
        Fill the specified location on the board with the player's mark.
        """
        if self.check_empty(loc):
            self.board[loc - 1] = player
        else:
            print('Picked Location has been filled. Please Change your choice.')

    def is_board_filled(self) -> bool:
        """
        Check if the board is completely filled.
        """
        return all(not str(item).isdigit() for item in self.board)

    def swap_player_turn(self) -> str:
        """
        Swap the turn between players.
        """
        if self.player_turn == self.players[0]:
            self.player_turn = self.players[1]
        else:
            self.player_turn = self.players[0]
        return self.player_turn

    def start(self) -> None:
        """
        Start the Tic Tac Toe game.
        """
        while True:
            self.show_board()
            loc = int(input(f"Player {self.player_turn} should mark the location (1-9): "))
            if loc < 1 or loc > 9:
                print('Your input is invalid')
                continue
            elif not self.check_empty(loc):
                print('Picked Location has been filled. Please Change your choice.')
                continue
            else:
                self.fill_stage(player=self.player_turn, loc=loc)
                if self.check_winner():
                    self.show_board()
                    break
                if self.is_board_filled() and not self.check_winner():
                    self.show_board()
                    print("It's a draw")
                    print('End Game')
                    break
                else:
                    self.player_turn = self.swap_player_turn()

if __name__ == '__main__':
    init(autoreset=True)
    game = TicTacToe()
    game.start()
