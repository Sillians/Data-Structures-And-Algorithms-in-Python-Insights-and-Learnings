# def fun1(a, b, c):
#     return a, b, c
#
# def fun2(*args):
#     args = list(args)
#     args[0] = "San Francisco"
#     args[1] = "California"
#
#     return fun1(*args)
#
# print(fun2('city', 'state', 'US America'))


def sum_values(a, b, c):
    sum_ = 0
    i = 0
    while i != 12:
        sum_ += i
    return sum_

# print(sum_values(8, 9, 10))

def dmod_lst(*args):
    args = list(args)
    n = [5, 6, 7]
    args[2] = [k*k for k in n]
    args[1] = [k**3 for k in n]

    return sum_values(*args)

print(dmod_lst(8, 9, 12))