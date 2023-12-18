from constants import SYMBOLS, SYMBOLS_TO_IGNORE

class Entity(object):

    def __init__(self):
        pass

    def GetTokenValue(self):
        pass


class Number(Entity):

    def __init__(self, number, positions):
        super().__init__()
        
        self.number_ = number
        self.positions_ = []
        for position in positions:
            self.positions_.append(Position(position))

    def GetTokenValue(self):
        return self.number_

class Position(object):

    def __init__(self, positionValue):
        self.positionValue_ = positionValue

class Symbol(Entity):
    
    def __init__(self, symbol, position):
        self.symbol_ = ""

        if symbol in SYMBOLS_TO_IGNORE:
            raise Exception(f"Character cannot be an ignored character. Character given: {symbol}")
        
        self.symbol_ = symbol
        self.position_ = Position(position)   

    def GetTokenValue(self):
        return self.symbol_

