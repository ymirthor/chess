class Tile:
    def __init__(self, id, name, x, y):
        self.name = name
        self.x = x
        self.y = y
        self.data = None
    
    def __str__(self):
        return str(self.x) +','+ str(self.y)
            
class Board:
    def __init__(self):
        self.board = self.generate_board()

    def __str__(self):
        return '\n'.join([' '.join([str(item).center(7) for item in line]) for line in self.board])

    def generate_board(self):
        letters = 'ABCDEFGH'
        numbers = '87654321'

        board = []
        for y, number in enumerate(numbers):
            row = []
            for x, letter in enumerate(letters):
                id = 0
                row.append(Tile(id, letter+number, x, y))
            board.append(row)
        return board
