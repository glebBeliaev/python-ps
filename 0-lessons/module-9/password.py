import string, random


def generate_password(length: int = 8, use_symbols: bool = True):
    if length < 6:
        return ""
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation
    chars = letters + digits
    if use_symbols:
        chars += symbols
    return "".join([random.choice(chars) for _ in range(length)])


print(generate_password(12, False))
