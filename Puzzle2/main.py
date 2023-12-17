# Jacob McKenna
# Advent of Code
# 12/16/23

import re
from game import Game

FILENAME = "input.txt"
GAME_FIELD = 0
ROUNDS_FIELD = 1
GAME_ID_REGEX = r"[0-9]+"

def ParseInput():
    file = open(FILENAME, "r")
    games = []

    for index, row in enumerate(file):
        hands = []
        # print(row)
        gameAndRounds = row.split(":")
        gameID = re.search(GAME_ID_REGEX, gameAndRounds[GAME_FIELD]).group()
        # print(gameID) 
        rounds = gameAndRounds[ROUNDS_FIELD].split(";")
        games.append(Game(gameID=gameID, gameRounds=rounds))





        

if __name__ == "__main__":
    ParseInput()