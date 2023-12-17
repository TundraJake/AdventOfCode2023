# Jacob McKenna
# Advent of Code
# 12/16/23

import re
from game import Game
from constants import *

MaxCubeInput =  {
    CUBE_COLORS.RED: 12,
    CUBE_COLORS.GREEN: 13,
    CUBE_COLORS.BLUE: 14
}

MinCubeInput = {
    CUBE_COLORS.RED: 0,
    CUBE_COLORS.GREEN: 0,
    CUBE_COLORS.BLUE: 0
}

def GetMinimumNumberOfCubeColorToPlay(game):
    cubeCounts = []
    for color, maxValue in MaxCubeInput.items():
        cubeCounts.append(game.GetMaxOfCubeColorSeen(color))
    # print(f"Extracted numbers: {cubeCounts}")
    return cubeCounts

def IsPossible(game):
    possible = True
    for color, maxValue in MaxCubeInput.items():
        if maxValue < game.GetMaxOfCubeColorSeen(color):
            possible = not possible
            break
    return possible

def SumPossibleGames(games):
    sumTotal = 0
    sumPowerTotal = 0

    for game in games:
        print(f"Checking Game {game.GetGameID()}...")

        if IsPossible(game):
            print(f"Adding game: {game.GetGameID()}")
            sumTotal += game.GetGameID()

        powerTotal = 1
        for num in GetMinimumNumberOfCubeColorToPlay(game):
            if num == 0:
                continue
            else:
                powerTotal = num * powerTotal

        sumPowerTotal += powerTotal
        

    return sumTotal, sumPowerTotal

        
    
def ParseInput():
    file = open(FILENAME, "r")
    games = []

    for index, row in enumerate(file):
        # print(row)
        gameAndRounds = row.split(":")
        gameID = int(re.search(GAME_ID_REGEX, gameAndRounds[GAME_FIELD]).group())
        # print(gameID) 
        rounds = gameAndRounds[ROUNDS_FIELD].split(";")
        games.append(Game(gameID=gameID, gameRounds=rounds))

    return games



        

if __name__ == "__main__":
    games = ParseInput()
    total, powerTotal = SumPossibleGames(games=games)
    print(total, powerTotal)