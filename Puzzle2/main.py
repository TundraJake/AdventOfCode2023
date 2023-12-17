# Jacob McKenna
# Advent of Code
# 12/16/23

import re
from game import Game

FILENAME = "input.txt"
GAME_FIELD = 0
ROUNDS_FIELD = 1
GAME_ID_REGEX = r"[0-9]+"

MaxCubeInput =  {
    "red": 12,
    "green": 13,
    "blue": 14
}

def SumPossibleGames(games):
    sumTotal = 0
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
            
    return sumTotal

        
    
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
    total = SumPossibleGames(games=games)
    print(total)