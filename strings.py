#!/usr/bin/env python
# Corey Goldberg - 2025
#
# Generate random string data for testing.

import random
import string
import unicodedata


# Unicode characters.
UNICODE = "".join(chr(i) for i in range(0x0000, 1 + 0xFFFF, 1))

# Unicode printable characters. A character is "printable" if it can be
# represented as a string without hex-escaping.
UNICODE_PRINTABLE = "".join(char for char in UNICODE if char.isprintable())

# Unicode whitespace characters. Includes characters in the Unicode character
# database, either a general category is Zs ('Separator, space'), or its
# bidirectional class is one of WS, B, or S.
UNICODE_WHITESPACE = "".join(char for char in UNICODE if char.isspace())

# ASCII printable characters. Includes uppercase letters, lowercase letters,
# digits, punctuation, and whitespace.
ASCII_PRINTABLE = string.printable

# ASCII uppercase and lowercase letters.
ASCII_LETTERS = string.ascii_letters

# ASCII lowercase letters.
ASCII_LOWERCASE = string.ascii_lowercase

# ASCII uppercase letters.
ASCII_UPPERCASE = string.ascii_uppercase

# ASCII characters which are considered punctuation characters in the C locale.
ASCII_PUNCTUATION = string.punctuation

# ASCII whitespace characters. Includes space, tab, linefeed, return, formfeed,
# and vertical tab.
ASCII_WHITESPACE = string.whitespace

# Digits 0-9.
DIGITS = string.digits

# Hexadecimal digits.
HEXDIGITS = string.hexdigits


def print_unicode_name_table(chars, width=30):
    """Prints a table of Unicode names and string representations
    from a sequence of characters.
    """
    print(f"{'Name':{width}}Character")
    print("-" * (width + 9))
    for char in chars:
        name = unicodedata.name(char, "Undefined").title()
        print(f"{name:{width}}{repr(char)}")


def random_string(chars, length=16):
    """Generates a random string of given length from a sequence of
    characters."""
    return "".join(random.choices(chars, k=length))
