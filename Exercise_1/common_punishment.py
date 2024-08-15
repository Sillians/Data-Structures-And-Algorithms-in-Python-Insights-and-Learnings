# A common punishment for school children is to write out a sentence mul- tiple times. 
# Write a Python stand-alone program that will write out the following sentence one hundred times: 
# “I will never spam my friends again.” Your program should number each of the sentences and it should make eight different random-looking typos.


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