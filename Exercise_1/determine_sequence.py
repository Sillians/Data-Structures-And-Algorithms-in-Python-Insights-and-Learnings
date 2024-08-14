from typing import List
def areDistinct(list_inp: List[int]) -> bool:
    uniqueNums = {x for x in list_inp}
    return len(uniqueNums) == len(list_inp)

list_inp = [100, 75, 100, 20, 75, 12, 75, 25]
print(areDistinct(list_inp))