from board import Board
from player import Player

class Game:
    def __init__(self):
        self.black = Player('Black')
        self.white = Player('White')
        self.board = Board()

    def start(self):
        pass


if __name__ == "__main__":
    g = Game()
    print(g.board)
