

def arithmetic_formula(a: int, b: int, c: int) -> str:
    result = []

    if a + b == c:
        result.append("a + b = c")
    if a == b - c:
        result.append("a = b - c")
    if a * b == c:
        result.append("a * b = c")
    if result:
        print("\n".join(result))
    else:
        print("No arithmetic formula found")


a = int(input("Type in your first char: "))
b = int(input("Type in your first char: "))
c = int(input("Type in your first char: "))
arithmetic_formula(a, b, c)
