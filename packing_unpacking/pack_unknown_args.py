def pack_unknown_args(*args):
    sqr = []
    for i in args:
        sqr.append(i**3)
    return sqr

print(pack_unknown_args(1, 2, 3, 4))


def unpack_unknown_args(*args):
    sum_ = 0
    for i in range(len(args)):
        sum_ += args[i]
    return sum_

print(unpack_unknown_args(1, 2, 3, 4))
