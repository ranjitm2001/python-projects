import re
from typing import Optional, Match


def validator(in_email: str) -> bool:
    # r@g.in -- Minimum valid length - 6
    if len(in_email) < 6:
        return False

    # email should start with an alphabet
    if not in_email[0].isalpha():
        return False

    # email should contain only one '@'
    if '@' not in in_email or in_email.count('@') != 1:
        return False

    # email last 3rd or 4th should be '.'
    if not ((in_email[-3] == '.') ^ (in_email[-4] == '.')):
        return False

    for letter in in_email:
        if letter == '@' or letter == '.' or letter == '_':
            # email contain only these three special characters
            continue
        elif letter.isdigit():
            # email can contain any number of digits
            continue
        elif letter.isspace():
            # email should not have spaces
            return False
        elif letter.isalpha() and letter.isupper():
            # email can't have upper case
            return False

    return True


def validator_regex(in_email: str) -> bool:
    # Not the way to do
    # length_condition = r"\b\w{6,}\b"
    # start_condition = r"^[a-z]"
    # asterisk_condition = r"\b\w+@\w+\b"
    # dot_condition = r"\b\w+\.\w{2,3}\b"
    # special_chars_condition = r"\b[a-z0-9@._]+\b"
    # space_condition = r"\b\S+\b"

    pattern = r"^[a-z][a-z0-9_.]+@[a-z]+\.[a-z]{2,3}$"
    return True if re.match(pattern, in_email) else False
