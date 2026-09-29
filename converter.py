from config import DIGITS


def convert(number, base):
    if number == 0:
        return "0"

    result = ""

    while number > 0:
        remainder = number % base
        result = DIGITS[remainder] + result
        number = number // base

    return result
