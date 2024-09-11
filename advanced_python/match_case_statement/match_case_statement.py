# A Python match-case statement takes an expression and compares its value to successive patterns given as one or more case blocks.

"""
Syntax:

match variable_name:
   case 'pattern 1' : statement 1
   case 'pattern 2' : statement 2
   ...
   case 'pattern n' : statement n
"""

def launched_apple_smartphone(year: int) -> str:
    match year:
        case 2007: return "iphone"
        case 2008: return "iPhone 3G"
        case 2009: return "iPhone 3GS"
        case 2010: return "iPhone 4"
        case 2011: return "iPhone 4s"
        case 2012: return "iPhone 5"
        case 2013: return "iPhone 5s series, iPhone 5c"
        case 2014: return "iPhone 6 series"
        case 2015: return "iPhone 6s series"
        case 2016: return "iPhone 7 series"
        case 2017: return "iPhone X, iPhone 8 series"
        case 2018: return "iPhone XR, iPhone XS series"
        case 2019: return "iPhone 11 series"
        case 2020: return "iPhone 12 series"
        case 2021: return "iPhone 13 series"
        case 2022: return "iPhone 14 series"
        case 2023: return "iPhone 15 series"
        case 2024: return "iPhone 16 series"
        case _:    return "No iPhone series released in this year yet"

year = int(input("Enter the year: "))
print(launched_apple_smartphone(year))

