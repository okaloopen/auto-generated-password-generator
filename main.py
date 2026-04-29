import random
import string
import sys


def generate_password(length: int = 12) -> str:
    """Generate a secure password containing uppercase, lowercase, digits and punctuation."""
    if length < 4:
        raise ValueError("Password length must be at least 4 to include all character types.")

    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    punctuation = string.punctuation

    # Start with one character of each type to ensure complexity
    password_chars = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(punctuation),
    ]

    # If more characters are needed, fill the rest from the full character set
    if length > 4:
        all_chars = lower + upper + digits + punctuation
        password_chars += random.choices(all_chars, k=length - 4)

    # Shuffle to avoid predictable placement
    random.shuffle(password_chars)
    return "".join(password_chars)


def main() -> None:
    """Entry point for the password generator."""
    # Determine length from command‑line argument if provided
    if len(sys.argv) > 1:
        try:
            length = int(sys.argv[1])
        except ValueError:
            print("Invalid length specified. Please provide an integer.")
            sys.exit(1)
    else:
        length = 12

    try:
        password = generate_password(length)
        print(password)
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
