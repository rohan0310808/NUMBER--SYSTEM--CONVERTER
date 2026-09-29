from converter import convert
from validation import get_number, get_base


def main():
    print("NUMBER SYSTEM CONVERTER")

    number = get_number()

    print("\nStandard Conversions")
    print("Binary:", convert(number, 2))
    print("Octal:", convert(number, 8))
    print("Hexadecimal:", convert(number, 16))

    print("\nCustom Base Conversion")
    base = get_base()

    print("Base", base, ":", convert(number, base))


if __name__ == "__main__":
    main()
