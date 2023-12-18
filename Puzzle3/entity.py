from constants import SYMBOLS, SYMBOLS_TO_IGNORE

class Entity(object):

    def __init__(self):
        pass

    def GetTokenValue(self):
        pass


class Number(Entity):

    def __init__(self, number, positions: list['Position']):
        super().__init__()
        
        self.number_ = number
        self.positions_ = positions
        
    def GetTokenValue(self):
        return self.number_

class Position(object):

    def __init__(self, rowIndex, colIndex):
        self.positionRowIndex_ = rowIndex
        self.positionColumnIndex_ = colIndex

class Symbol(Entity):
    
    def __init__(self, symbol, rowIndex, position):
        self.symbol_ = ""

        if symbol in SYMBOLS_TO_IGNORE:
            raise Exception(f"Character cannot be an ignored character. Character given: {symbol}")
        
        self.symbol_ = symbol
        self.position_ = Position(rowIndex, position)

    def GetTokenValue(self):
        return self.symbol_

