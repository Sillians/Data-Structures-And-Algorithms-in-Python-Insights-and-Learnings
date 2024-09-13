from time import time
start_time = time( ) # record the starting time
print(start_time)

# run algorithm
def sample_algorightm(n: list) -> list:
    arr = [(i**(1/2)) for i in n]
    return arr

n = [22, 45, 67, 89, 12, 15]
print(sample_algorightm(n))

end_time = time( ) # record the ending time
print(end_time)

elapsed = end_time - start_time # compute the elapsed time
print(elapsed)
