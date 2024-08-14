from typing import  List

def reverse_order() -> List:
    data = []
    while True:
        try:
            data.append(input())
        except EOFError:
            break
    print(list(reversed(data)))

reverse_order()