import random


def generate_password(length, use_digits, use_special):
    """
    Generate a random password with customizable options.

    @param length (int): The length of the password.
    @param use_digits (bool): Whether to include digits (0-9)
    @param use_special (bool): Whether to include special characters

    @return (str): Randomly generated password.
    """

    # possible character strings
    lower_letters = "abcdefghijklmnopqrstuvwxyz"
    upper_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digits = "0123456789"
    specials = "!@#$%^&*()_+"

    possible_characters = ""
    # TODO: concat lower_letters and upper_letters into 'possible_characters'
    possible_characters += lower_letters + upper_letters

    # TODO: if 'use_digits' is True, concat 'digits' to 'possible_characters'
    if use_digits:
        possible_characters += digits

    # TODO: if 'use_special' is True, concat 'specials' to 'possible_characters'
    if use_special:
        possible_characters += specials

    # TODO: build a list from 'possible_characters' so that each character is a list item
    char_list = list(possible_characters)

    password = ""
    # TODO: use loop to generate the random password
    for _ in range(length):
        password += random.choice(char_list)

    return password


if __name__ == "__main__":
    print(generate_password(12, True, True))    # length 12, include digits + special chars
    print(generate_password(14, True, False))   # length 14, include digits, no special chars
    print(generate_password(16, False, True))   # length 16, include special chars, no digits
    print(generate_password(18, False, False))  # length 18, letters only
