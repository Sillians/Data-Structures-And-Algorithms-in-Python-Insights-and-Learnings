import itertools
from typing import List

def generate_permutations(characters: List[str]) -> str:
    permutations = itertools.permutations(characters)
    for perm in permutations:
        print(''.join(perm))

characters = ['c', 'a', 't', 'd', 'o', 'g']
generate_permutations(characters)