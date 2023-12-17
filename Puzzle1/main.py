# Jacob McKenna
# Advent of Code - Puzzle 1
# Works for both puzzles. Assign the alphaFlag to True for alphanumeric characters.
# 12/16/23
from valid_digits import VALID_DIGITS, VALID_FIRST_CHARS

FILE_NAME = "input.txt"

def SumFirstAndLastDigits(numbersList):
    sumTotal = 0
    for number in numbersList:
        currentSum = 0
        # print("Number to operate on: ", number)
        numDigits = len(number)
        if numDigits == 1:
           currentSum += int(number + number)
        else:
            currentSum += int(number[0] + number[-1])
        # print("Sum Result: ", currentSum)
        sumTotal += currentSum
    return sumTotal 

def ExtractNumberInRow(alphaFlag=None, row=None):
    foundNumbers = ""
    position = 0
    maxRowLength = len(row)
    while position < maxRowLength:
        currentChar = row[position]
        # print(currentChar, type(currentChar))
        if currentChar.isdigit():
            foundNumbers += currentChar
        
        elif alphaFlag and currentChar.isalpha() and currentChar in VALID_FIRST_CHARS:
            potentialNumber = currentChar
            position += 1
            while True:
    
                if position == maxRowLength:
                    break
                
                nextChar = row[position]
                if nextChar.isdigit():
                    position -= len(potentialNumber)
                    break
                
                elif nextChar.isalpha():
                    potentialNumber += nextChar
                    position += 1


                    if potentialNumber in VALID_DIGITS:
                        foundNumbers += VALID_DIGITS[potentialNumber]
                        # -2 accounts for shared chars, such as 'oneight'
                        position -= 2
                        break

                    elif len(potentialNumber) == 5:
                        position -= len(potentialNumber)
                        break

                    elif position == maxRowLength:
                        position -= len(potentialNumber)
                        break
        position += 1
    return foundNumbers

def ReadFile():
    file = open(FILE_NAME, 'r')   
    numbersList = []

    for index, row in enumerate(file):
        row = row.strip('\n')
        numbersList.append(ExtractNumberInRow(True, row))
        # print("To process: ", row)
        # print("Processed: ", numbersList[index])
        print(numbersList[index])

    return numbersList 

if __name__ == "__main__":
    numbers = ReadFile()
    print(SumFirstAndLastDigits(numbers))