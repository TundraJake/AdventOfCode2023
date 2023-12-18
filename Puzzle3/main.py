# Jacob McKenna
# Advent of Code
# 12/16/23

from constants import *
from entity import Symbol, Number, Position
import re 

def DetermineAdjacency(symbolTokens, numberTokens):
    sum = 0
    for symbol in symbolTokens:
        for number in numberTokens:
            if symbol.GetPosition() in number.GetAdjacentPositions() and number.MayAdd():
                sum += number.GetTokenValue()

        print(f"Current sum {sum}")

    return sum


def CreateTokens(rowIndex, row, symbolTokens, numberTokens):
    position = 0
    numChars = len(row)
    currentNumber = ""
    currentNumberPositions = []
    while position < numChars:
        currentChar = row[position]
        print(f"working position {position}")
        if currentChar.isdigit():
            currentNumber += currentChar
            currentNumberPositions.append(Position(rowIndex, position))
            if position + 1 == numChars:
                numberTokens.append(Number(currentNumber, currentNumberPositions))
            elif row[position + 1] in SYMBOLS_TO_IGNORE or row[position + 1] in SYMBOLS:
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
                    
    # PrintTokens(symbolTokens)
    # PrintTokens(numberTokens)
    return symbolTokens, numberTokens
                        
if __name__ == "__main__":
    symbolTokens, numberTokens = ParseInput()
    sum = DetermineAdjacency(symbolTokens, numberTokens)
    print(f"The sum is: {sum}")