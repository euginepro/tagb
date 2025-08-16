import random
import string


def random_grease_brand():
    """
    Generates a random GREASE-style brand for Sec-CH-UA.
    Mimics Chrome's behavior, e.g., " Not A;Brand".
    """
    # Some base templates Chrome uses
    templates = [
        " Not A;Brand",
        " Not:A-Brand",
        " Not-A.Brand",
        " Unknown;Brand"
    ]

    # Pick a random template
    base = random.choice(templates)

    # Optionally add a random suffix or number for extra randomness
    suffix = ''.join(random.choices(string.ascii_letters + string.digits, k=random.randint(5, 10)))

    return f'"{base}{suffix}"'

"""
# Example usage
for _ in range(5):
    print(random_grease_brand())"""
