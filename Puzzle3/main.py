# Jacob McKenna
# Advent of Code
# 12/16/23

from constants import *
from entity import Symbol, Number, Position
import re 

def CalculateSumPuzzlePart2():
    sum = 0
    for symbol in symbolTokens:
        
        if symbol.GetTokenValue() == MULTIPLY_SYMBOL:
            integersToMultiply = []
            for number in numberTokens:
                if symbol.GetPosition() in number.GetAdjacentPositions() and number.MayAdd():
                    integersToMultiply.append(number.GetTokenValue())
                    
                    if len(integersToMultiply) == 2:
                        sum += integersToMultiply[0] * integersToMultiply[-1] 

        print(f"Current sum {sum}")

    return sum

def CalculateSumPuzzlePart1():
    sum = 0
    for symbol in symbolTokens:
        for number in numberTokens:
            if symbol.GetPosition() in number.GetAdjacentPositions() and number.MayAdd():
                sum += number.GetTokenValue()

        print(f"Current sum {sum}")

    return sum

def RunPuzzle(symbolTokens, numberTokens, puzzleType):
    if puzzleType == PUZZLE_TYPE.PUZZLE_ONE:
        return CalculateSumPuzzlePart1()
    return CalculateSumPuzzlePart2()


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
    sum = RunPuzzle(symbolTokens, numberTokens, PUZZLE_TYPE.PUZZLE_TWO)
    print(f"The sum is: {sum}")