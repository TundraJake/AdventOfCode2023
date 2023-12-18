# Jacob McKenna
# Advent of Code
# 12/16/23

from constants import *
from entity import Symbol, Number, Position
import re 

def CreateTokens(rowIndex, row, symbolTokens, numberTokens):
    position = 0
    numChars = len(row)
    currentNumber = ""
    currentNumberPositions = []
    while position < numChars:
        currentChar = row[position]

        if currentChar.isdigit():
            currentNumber += currentChar
            currentNumberPositions.append(Position(rowIndex, position))
            if row[position + 1] in SYMBOLS_TO_IGNORE or row[position + 1] in SYMBOLS:
                # print(currentNumber)
                numberTokens.append(Number(currentNumber, currentNumberPositions))
                currentNumber = ""
                currentNumberPositions = []
        elif currentChar in SYMBOLS:
            # print(f"Symbol: {currentChar}")
            symbolTokens.append(Symbol(currentChar, rowIndex, position))
        elif not (currentChar in SYMBOLS_TO_IGNORE):
            raise Exception(f"Unrecognized character: {currentChar}")
        
        position += 1

    # print(f"Tokens processed: {tokens}")

def PrintTokens(tokens):
    for token in tokens:
        print(token.GetTokenValue())

def ParseInput():
    symbolTokens = []
    numberTokens = []
    with open(FILENAME) as file:
        for rowIndex, row in enumerate(file):
            row = row.strip("\n")
            CreateTokens(rowIndex, row, symbolTokens, numberTokens)
                    
    PrintTokens(symbolTokens)
    PrintTokens(numberTokens)
    return symbolTokens, symbolTokens
                        
if __name__ == "__main__":
    symbolTokens, symbolTokens = ParseInput()