def calulator(sign, a, b):
    def add(a, b):
        return a + b

    def mines(a, b):
        return a - b

    def multiple(a, b):
        return a * b

    def divide(a, b):
        return a // b

    match sign:
        case "+":
            return add(a, b)
        case "-":
            return mines(a, b)
        case "*":
            return multiple(a, b)
        case "/":
            return divide(a, b)
        case _:
            return None


result = calulator("+", 2, 4)
print(result)
