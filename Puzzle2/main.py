# Jacob McKenna
# Advent of Code
# 12/16/23

import re
from game import Game
from constants import CUBE_COLORS

FILENAME = "input.txt"
GAME_FIELD = 0
ROUNDS_FIELD = 1
GAME_ID_REGEX = r"[0-9]+"

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

def SumPossibleGames(games):
    sumTotal = 0
    sumPowerTotal = 0
    cubeCounts = []
    possible = True
    for game in games:
        possible = True
        print(f"Checking Game {game.GetGameID()}...")
        for color, maxValue in MaxCubeInput.items():
            if maxValue < game.GetMaxOfCubeColorSeen(color):
                possible = not possible
                break
        
        if possible:
            print(f"Adding game: {game.GetGameID()}")
            sumTotal += game.GetGameID()
        
        for color, maxValue in MaxCubeInput.items():
            cubeCounts.append(game.GetMaxOfCubeColorSeen(color))

        powerTotal = 1
        print(f"Extracted numbers: {cubeCounts}")
        for num in cubeCounts:
            
            if num == 0:
                continue
            else:
                powerTotal = num * powerTotal

        sumPowerTotal += powerTotal
        powerTotal = 0
        cubeCounts = []
        

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