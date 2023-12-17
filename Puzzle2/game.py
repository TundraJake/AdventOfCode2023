import re

HAND_NUMBER_REGEX = r"[0-9]+"
class CUBE_COLORS(object):
    RED = "red"
    GREEN = "green"
    BLUE = "blue"

class GameRound(object):

    def __init__(self, round):

        # print(round)
        self.numRedCubes_ = 0
        self.numGreenCubes_ = 0
        self.numBlueCubes_ = 0        
        
        hands = round.split(",")
        
        for hand in hands:
            if CUBE_COLORS.RED in hand:
                self.numRedCubes_ = re.search(HAND_NUMBER_REGEX, hand).group()
            if CUBE_COLORS.GREEN in hand:
                self.numGreenCubes_ = re.search(HAND_NUMBER_REGEX, hand).group()
            if CUBE_COLORS.BLUE in hand:
                self.numBlueCubes_ = re.search(HAND_NUMBER_REGEX, hand).group()

        # print(f"Red: {self.numRedCubes_} Green: {self.numGreenCubes_} Blue: {self.numBlueCubes_}")


class Game(object):
    
    def __init__(self, gameID, gameRounds):
        self.gameID_ = gameID
        self.gameRounds_ = []
        # print(self.GetGameID())
        for round in gameRounds:
            self.gameRounds_.append(GameRound(round))


    def GetGameID(self):
        return self.gameID_