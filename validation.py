def get_number():
    while True:
        try:
            number = int(input("Enter a non-negative decimal number: "))

            if number >= 0:
                return number

            print("Please enter a non-negative number.")

        except ValueError:
            print("Please enter a valid integer.")


def get_base():
    while True:
        try:
            base = int(input("Enter a base between 2 and 16: "))

            if 2 <= base <= 16:
                return base

            print("Base must be between 2 and 16.")

        except ValueError:
            print("Please enter a valid base.")
