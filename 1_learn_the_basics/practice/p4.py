import random


def guess_number():
    """بازی حدس عدد بین 1 تا 100"""
    target = random.randint(1, 100)
    attempts = 0

    while True:
        guess = int(input("حدس شما (1-100): "))
        attempts += 1

        if guess < target:
            print("بزرگتر!")
        elif guess > target:
            print("کوچکتر!")
        else:
            return f"آفرین! عدد {target} را در {attempts} بار حدس زدید."


# اجرای بازی
print(guess_number())
