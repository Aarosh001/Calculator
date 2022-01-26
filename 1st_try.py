
def add(n1, n2):
    return n1 + n2


def sub(n1, n2):
    return n1 - n2


def mul(n1, n2):
    return n1 * n2


def div(n1, n2):
    return n1 / n2


def exp(n1, n2):
    return n1 ** n2


cond = True
dictn = {"+": add, "-": sub, "*": mul, "/": div, "**": exp}
num1 = float(input("Enter first number: "))
while cond:
    for item in dictn:
        print(item)
    op = input("Select an operation: ")
    if op not in dictn:
        print("Invalid Operation ")
        exit()
    num2 = float(input("Enter second number: "))
    answer = dictn[op](num1, num2)
    print(f"{num1} {op} {num2} = {answer}")
    if input("Press y to do further calculations, any other key to exit: ") != "y":
        cond = False
    num1 = answer

