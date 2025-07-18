def calculator():
    """یک ماشین حساب ساده"""
    print("عملیات موجود: +, -, *, /")
    num1 = float(input("عدد اول: "))
    op = input("عملگر: ")
    num2 = float(input("عدد دوم: "))

    if op == "+":
        return num1 + num2
    elif op == "-":
        return num1 - num2
    elif op == "*":
        return num1 * num2
    elif op == "/":
        return num1 / num2
    else:
        return "عملگر نامعتبر"


# اجرای ماشین حساب
print(calculator())
