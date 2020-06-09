class Piece:
    def __init__(self, id):
        self.id = id

    def __str__(self):
        return self.__class__.__name__

class Pawn(Piece):
    points = 1
    def movement(self):
        pass

class Knight(Piece):
    points = 3
    def movement(self):
        logic = abs(xx - self.x) == 2 and abs(yy - self.y) == 1 or abs(yy - self.y) == 2 and abs(xx - self.x) == 1

class Bishop(Piece):
    points = 3
    def movement(self):
        logic = self.x + self.y == xx + yy or self.x - self.y == xx - yy

class Rook(Piece):
    points = 5
    def movement(self):
        logic = self.x == xx or self.y == yy

class Queen(Piece):
    points = 9
    def movement(self):
        logic = self.x + self.y == xx + yy or self.x - self.y == xx - yy or self.x == xx or self.y == yy

class King(Piece):
    points = 1000
    def movement(self):
        logic = abs(xx - self.x) <= 1 and abs(yy - self.y) <= 1

