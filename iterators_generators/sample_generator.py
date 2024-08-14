def square_generator(sequence):
    for item in sequence:
        yield item**2

for square in square_generator([3, 4, 6, 8, 10]):
    print(square)