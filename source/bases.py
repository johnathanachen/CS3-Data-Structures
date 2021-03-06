#!python

import string
import math

# Hint: Use these string constants to encode/decode hexadecimal digits and more
# string.digits is '0123456789'
# string.hexdigits is '0123456789abcdefABCDEF'
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase
# string.printable is digits + ascii_letters + punctuation + whitespace


def decode(digits, base):
    """Decode given digits in given base to number in base 10.
    digits: str -- string representation of number (in given base)
    base: int -- base of given number
    return: int -- integer representation of number (in base 10)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)

    number_base_10 = 0

    for i in range(0, len(digits)):
        # ith index letter
        digit = digits[i]
        # alphabet or digit
        if digit.isalpha():
            # lowercase or uppercase
            if digits.islower():
                # base number powered by ((len(digits) - 1) - i) place value
                number_base_10 += base ** ((len(digits) - 1) - i) * (string.ascii_letters.index(digit) + 10)
            else:
                #
                number_base_10 += base ** ((len(digits) - 1) - i) * (string.ascii_letters.index(digit) + 10 - 26)
        else:
            #
            number_base_10 += base ** ((len(digits) - 1) - i) * int(digit)
    return number_base_10




def encode(number, base):
    """Encode given number in base 10 to digits in given base.
    number: int -- integer representation of number (in base 10)
    base: int -- base to convert to
    return: str -- string representation of number (in given base)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    # Handle unsigned numbers only for now
    assert number >= 0, 'number is negative: {}'.format(number)

    encoded_number = ""
    while number != 0:
        # calculate remainder
        remainder = number % base
        print("R: {}".format(remainder))
        if remainder >= 10:
            # get alphabet character
            remainder = string.ascii_letters[remainder - 10]
        # prepend remainder to encoded_number
        encoded_number = str(remainder) + encoded_number
        # round down
        number = int(number / base)
        print("N: {}".format(number / base))
    return encoded_number


def convert(digits, base1, base2):
    """Convert given digits in base1 to digits in base2.
    digits: str -- string representation of number (in base1)
    base1: int -- base of given number
    base2: int -- base to convert to
    return: str -- string representation of number (in base2)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base1 <= 36, 'base1 is out of range: {}'.format(base1)
    assert 2 <= base2 <= 36, 'base2 is out of range: {}'.format(base2)

    decoded_number = decode(digits, base1)
    encoded_number = encode(decoded_number, base2)
    return encoded_number


def main():
    """Read command-line arguments and convert given digits between bases."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 3:
        digits = args[0]
        base1 = int(args[1])
        base2 = int(args[2])
        # Convert given digits between bases
        result = convert(digits, base1, base2)
        print('{} in base {} is {} in base {}'.format(digits, base1, result, base2))
    else:
        print('Usage: {} digits base1 base2'.format(sys.argv[0]))
        print('Converts digits from base1 to base2')


if __name__ == '__main__':
    main()
