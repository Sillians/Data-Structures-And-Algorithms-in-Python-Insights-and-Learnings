# ** is used for unpacking dictionaries
# def unpac_dictionary(a, b, c):
#     print(a, b, c)
#
# unpack = {"a":"Hello", "b":"City", "c":"of San Francisco"}
# unpac_dictionary(**unpack)


def square(*args):
    for i in range(len(args)):
        return args[i] ** 2

def sum_(*args):
    sum_value = 0
    for i in range(len(args)):
        sum_value += args[i]
    return sum_value
def unpack(a, b, c, d):
    # return sum_(a, b, c, d)
    return square(a, b, c, d)

un = {'a':12, 'b':15, 'c':3, 'd':9}
vn = unpack(**un)
# square(vn)
print(vn)
