lst = list(range(10))
iterator = iter(lst)
while True:
    try:
        item = next(iterator)
    except StopIteration:
        break
    else:
        print(item)
