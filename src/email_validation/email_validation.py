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
