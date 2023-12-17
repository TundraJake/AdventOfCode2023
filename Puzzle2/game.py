import re

HAND_NUMBER_REGEX = r"[0-9]+"
HAND_COLOR_REGEX = r"[a-z]+"

class GameRound(object):

    def __init__(self, round):

        # print(round)
        self.handDescription_ = {}
        
        hands = round.split(",")
        
        for hand in hands:
            numCubes = int(re.search(HAND_NUMBER_REGEX, hand).group())
            colorOfCubes = re.search(HAND_COLOR_REGEX, hand).group()
            self.handDescription_[colorOfCubes] = numCubes

        # print(self.handDescription_)
            
    def GetCubes(self, color):
        try:
            return self.handDescription_[color]
        except:
            return 0

class Game(object):
    
    def __init__(self, gameID, gameRounds):
        self.gameID_ = gameID
        self.gameRounds_ = []

        # print(self.GetGameID())
        for round in gameRounds:
            self.gameRounds_.append(GameRound(round))
    
    def GetMaxOfCubeColorSeen(self, color):
        maxCount = 0
        for round in self.GetGameRounds():
            count = round.GetCubes(color)
            if maxCount < count:
                maxCount = count
        return maxCount
    
    def GetGameRounds(self):
        return self.gameRounds_

    def GetGameID(self):
        return self.gameID_