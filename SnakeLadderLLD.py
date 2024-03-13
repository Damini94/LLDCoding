
'''

Propose LLD with python code following all SOLID principle and design patterns for snake and ladder games. requirements are listed below :

Customizable Board in terms of snake and ladder placement and Board size

Customizable in terms of number of dice used

When Game Board loads it should :

A. Load the configured Board size

B. Load the configured snake and ladder

C. Load the configured number of dice

D. Load the number of players who will play the game and all players should be at starting

'''

from typing import List, Tuple
import random

class Square:
    def __init__(self, number: int):
        self.number = number
        self.snake = None
        self.ladder = None

    def set_snake(self, end: int):
        self.snake = end

    def set_ladder(self, end: int):
        self.ladder = end

class Dice:
    def __init__(self, faces: int = 6):
        self.faces = faces

    def roll(self) -> int:
        return random.randint(1, self.faces)

class Player:
    def __init__(self, name: str):
        self.name = name
        self.position = 0

class Board:
    def __init__(self, size: int, snakes: List[Tuple[int, int]], ladders: List[Tuple[int, int]]):
        self.size = size
        self.squares = [Square(i) for i in range(1, size + 1)]
        for start, end in snakes:
            self.squares[start - 1].set_snake(end)
        for start, end in ladders:
            self.squares[start - 1].set_ladder(end)

class Game:
    def __init__(self, board: Board, players: List[Player], dice: Dice):
        self.board = board
        self.players = players
        self.dice = dice

    def play_turn(self, player: Player) -> bool:
        roll = self.dice.roll()
        print(f"{player.name} rolls {roll}")
        player.position += roll
        if player.position > self.board.size:
            player.position = self.board.size - (player.position - self.board.size)
        print(f"{player.name} is now at square {player.position}")
        square = self.board.squares[player.position - 1]
        if square.snake:
            print(f"{player.name} got bitten by a snake! Moving to square {square.snake}")
            player.position = square.snake
        elif square.ladder:
            print(f"{player.name} climbed a ladder! Moving to square {square.ladder}")
            player.position = square.ladder
        return player.position == self.board.size

if __name__ == "__main__":
    # Example usage
    snakes = [(16, 6), (47, 26), (49, 11), (56, 53), (62, 19), (64, 60), (87, 24), (93, 73), (95, 75), (98, 78)]
    ladders = [(1, 38), (4, 14), (9, 31), (21, 42), (28, 84), (36, 44), (51, 67), (71, 91), (80, 100)]
    board_size = 100
    board = Board(board_size, snakes, ladders)
    dice = Dice()
    players = [Player("Player 1"), Player("Player 2")]
    game = Game(board, players, dice)

    while True:
        for player in players:
            if game.play_turn(player):
                print(f"{player.name} wins!")
                exit()
