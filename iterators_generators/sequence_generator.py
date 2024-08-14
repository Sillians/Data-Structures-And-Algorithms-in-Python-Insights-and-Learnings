def sequence_generator(sequence):
    for item in sequence:
        yield item

sequence_generator([1, 2, 3, 4, 5])
for number in sequence_generator([1, 2, 3, 4, 5]):
    print(number)