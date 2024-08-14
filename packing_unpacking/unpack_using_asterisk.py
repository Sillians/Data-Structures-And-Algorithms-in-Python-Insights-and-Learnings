def fun(a, b, c, d):
    for i in a, b, c, d:
        print(i**2)


my_list = [1, 2, 3, 4]
fun(*my_list)


new_lst = [1, 2, 3]
print(range(*new_lst))