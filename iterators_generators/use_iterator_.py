from sequence_iter import SequenceIterator

sequence = SequenceIterator([4, 5, 6, 7])
iterator = sequence.__iter__()
while True:
    try:
        item = iterator.__next__()
    except StopIteration:
        break
    else:
        print(item)
