from pieces import *

class Player:
    def __init__(self, name):
        self.name = name
        self.pieces = self.create_pieces()

    def create_pieces(self):
        pieces = []

        create_piece = {
            1: King,
            2: Queen,
            3: Bishop,
            4: Bishop,
            5: Knight,
            6: Knight,
            7: Rook,
            8: Rook,
        }

        for i in range(1, 17):
            if i <= 8:
                piece = create_piece[i](i)
            else:
                piece = Pawn(i)
            pieces.append(piece)

        return pieces