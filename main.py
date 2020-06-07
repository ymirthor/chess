class Player:
    def __init__(self, is_white, placement):
        self.is_white = is_white
        self.placement = placement

    def __str__(self):
        return self.__class__.__name__

class Pawn(Player):
    points = 1
    def get_moves(self):
        pass

class Knight(Player):
    points = 3

class Bishop(Player):
    points = 3

class Rook(Player):
    points = 5

class Queen(Player):
    points = 9

class King(Player):
    points = 1000

class Tile:
    def __init__(self, name):
        self.player = self.place_on_tile(name)
        self.name = name
    
    def __str__(self):
        return f'{str(self.player or ""):9}'

    def place_on_tile(self, tile_name):
        if tile_name in ['A8', 'H8']:
            return Rook(
                is_white=False, 
                placement=tile_name,
            )

        if tile_name in ['B8', 'G8']:
            return Knight(
                is_white=False,
                placement=tile_name,
            )

        if tile_name in ['C8', 'F8']:
            return Bishop(
                is_white=False,
                placement=tile_name,
            )

        if tile_name == 'D8':
            return Queen(
                is_white=False,
                placement=tile_name,
            )
        
        if tile_name == 'E8':
            return King(
                is_white=False,
                placement=tile_name,
            )

        if tile_name[1] == '7':
            return Pawn(
                is_white=False,
                placement=tile_name,
            )

        if tile_name in ['A1', 'H1']:
            return Rook(
                is_white=True, 
                placement=tile_name,
            )

        if tile_name in ['B1', 'G1']:
            return Knight(
                is_white=True,
                placement=tile_name,
            )
        
        if tile_name in ['C1', 'F1']:
            return Bishop(
                is_white=True,
                placement=tile_name,
            )
        
        if tile_name == 'D1':
            return Queen(
                is_white=True,
                placement=tile_name,
            )
        
        if tile_name == 'E1':
            return Knight(
                is_white=True,
                placement=tile_name,
            )

        if tile_name[1] == '2':
            return Pawn(
                is_white=True,
                placement=tile_name,
            )

class Board:
    def __init__(self):
        self.board = self.generate_board()

    def generate_board(self):
        letters = 'ABCDEFGH'
        numbers = '87654321'

        print(end='  ')
        for letter in letters:
            print(f'{letter:9}', end=' ')
        print()

        for number in numbers:
            print(f'{number}', end=' ')
            for letter in letters:
                print(Tile(letter+number), end=' ')
            print()

if __name__ == "__main__":
    Board()