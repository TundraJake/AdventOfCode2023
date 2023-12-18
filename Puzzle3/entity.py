from constants import SYMBOLS, SYMBOLS_TO_IGNORE

class Entity(object):

    def __init__(self):
        pass

    def GetTokenValue(self):
        pass


class Number(Entity):

    def __contains__(self, key):
        positions = []
        for pos in self.GetPositions():
            positions.append(pos.GetCoordinates())
        return key in positions

    def __init__(self, number, positions: list['Position']):
        super().__init__()
        
        self.number_ = int(number)
        self.positions_ = positions
        self.added_ = False
    
    def MayAdd(self):
        if not self.__GetAdded():
            self.SetAdded(True)
            return self.GetTokenValue() 
        return 0
    
    def SetAdded(self, bool):
        self.added_ = bool

    def GetTokenValue(self):
        return self.number_
    
    def __GetAdded(self):
        return self.added_
    
    def GetPositions(self):
        return self.positions_

    def GetAdjacentPositions(self):
        adjacentRowHeight = 3
        adjacentRowLength = 3
        adjacenctPositions = []
        excludedPositions = []
        for position in self.GetPositions():
            for colJ in range(adjacentRowHeight):
                for rowI in range(adjacentRowLength):
                    if colJ == 0:
                        i = position.GetICoordinate() - 1
                        j = position.GetJCoordinate() + rowI - 1
                    elif colJ == 1:
                        i = position.GetICoordinate() 
                        j = position.GetJCoordinate() + rowI - 1
                    elif colJ == 2:
                        i = position.GetICoordinate() + 1
                        j = position.GetJCoordinate() + rowI - 1

                    newPosition = Position(i,j)
                    if not newPosition in self.GetPositions():
                        adjacenctPositions.append(newPosition)
                    else:
                        excludedPositions.append(newPosition)

        adjacenctPositions = set(adjacenctPositions)
        excludedPositions = set(excludedPositions)
        gridString = ""
        for index, pos in enumerate(adjacenctPositions):
            gridString += pos.PrintCoordinates().strip("\n")
            
        print(gridString)
        for excludePos in excludedPositions:
            print(excludePos.PrintCoordinates())
        return adjacenctPositions
    
class Position(object):

    def __eq__(self, rhs):
        return self.GetICoordinate() == rhs.GetICoordinate() and self.GetJCoordinate() == rhs.GetJCoordinate()

    # Used to call 'set' function and removed duplicates. 
    def __hash__(self):
        return hash(self.GetCoordinates())

    def __init__(self, i, j):
        self.i_ = i
        self.j_ = j

    def PrintCoordinates(self):
        return f"[{self.i_} , {self.j_}]"
    
    def GetCoordinates(self):
        return f"[{self.i_} , {self.j_}]"

    def GetICoordinate(self):
        return self.i_
    
    def GetJCoordinate(self):
        return self.j_
    


class Symbol(Entity):
    
    def __init__(self, symbol, rowIndex, position):
        self.symbol_ = ""

        if symbol in SYMBOLS_TO_IGNORE:
            raise Exception(f"Character cannot be an ignored character. Character given: {symbol}")
        
        self.symbol_ = symbol
        self.position_ = Position(rowIndex, position)

    def GetTokenValue(self):
        return self.symbol_
    
    def GetPosition(self):
        return self.position_

