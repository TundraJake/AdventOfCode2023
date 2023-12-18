# Jacob McKenna
# Advent of Code
# 12/16/23

from constants import *
from entity import Symbol, Number
import re 

def CreateTokens(row):
    position = 0
    numChars = len(row)
    currentNumber = ""
    currentNumberPositions = []
    tokens = []
    while position < numChars:
        currentChar = row[position]

        if currentChar.isdigit():
            currentNumber += currentChar
            currentNumberPositions.append(position)
            if row[position + 1] in SYMBOLS_TO_IGNORE or row[position + 1] in SYMBOLS:
                # print(currentNumber)
                tokens.append(Number(currentNumber, currentNumberPositions))
                currentNumber = ""
                currentNumberPositions = []
        elif currentChar in SYMBOLS:
            # print(f"Symbol: {currentChar}")
            tokens.append(Symbol(currentChar, position))
        elif not (currentChar in SYMBOLS_TO_IGNORE):
            raise Exception(f"Unrecognized character: {currentChar}")
        
        position += 1

    # print(f"Tokens processed: {tokens}")
    return tokens

def PrintTokens(tokens):
    for token in tokens:
        print(token.GetTokenValue())

def ParseInput():
    tokens = []
    with open(FILENAME) as file:
        for row in file:
            row = row.strip("\n")
            for token in CreateTokens(row):
                tokens.append(token)
                    
    # PrintTokens(tokens)
    return tokens
                        
if __name__ == "__main__":
    tokens = ParseInput()