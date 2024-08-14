
def packing_dictionaries(**kwargs):

    # kwargs is a dict
    print(type(kwargs))

    # Printing dictionary items
    for key, value in kwargs.items():
        print("%s = %s" % (key, value))

packing_dictionaries(city="San Francisco", country="US America", population=3424232, state="California")