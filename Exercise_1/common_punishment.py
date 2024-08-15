from random import randrange, randint

def error(sentence: str) -> str:
    errorchar = randrange(ord('a'), ord('a')+26)
    errorlocation = randint(0, len(sentence))
    newsentence = f'{sentence[:errorlocation-1]}{chr(errorchar)}{sentence[errorlocation:]}'
    return newsentence

def punishment(numlines: int, numerror: int) -> str:
    errorlineid = [randint(0, numlines) for i in range(numerror)]
    sentence = "I will never spam my friends again"
    for i in range(numlines):
        if i in errorlineid:
            print(f'{i} {error(sentence)} <-- Typo Line')
        else:
            print(f'{i}', sentence)


numlines = 100
numerror = 8
punishment(numlines, numerror)