# The birthday paradox says that the probability that two people in a room will have the same birthday is more than half,
# provided n, the number of people in the room, is more than 23. This property is not really a paradox,
# but many people find it surprising. Design a Python program that can test this paradox by a series of
# experiments on randomly generated birthdays, which test this paradox for n = 5,10,15,20,...,100.

def birthday_paradox(n: int) -> float:
    prob = 1
    for i in range(0,n):
        prob*=(365-i)/365
    return 1-prob

nlist = [i*5 for i in range(1,21)]
for n in nlist:
  print(f'{n}:', round(birthday_paradox(n), 5))