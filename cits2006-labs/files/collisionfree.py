import hashlib
import random
import string

# Collision resistance: it is hard to find ANY two messages x1 != x2 with H(x1) = H(x2).
# As in oneway.py, compare only the first HEX_DIGITS hex digits of MD5, so a collision is findable.
HEX_DIGITS = 4
TRIALS = 20  # increase for a better average
ALPHABET = string.ascii_letters + string.digits + string.punctuation


def random_message(length=16):
    return ''.join(random.choice(ALPHABET) for _ in range(length))


def tries_to_collide(hex_digits=HEX_DIGITS):
    """Return how many random messages you hashed before two different ones shared the same prefix."""
    # YOUR CODE GOES HERE
    raise NotImplementedError


if __name__ == '__main__':
    total = 0
    for i in range(TRIALS):
        tried = tries_to_collide()
        print(f"run {i+1}: {tried}")
        total += tried
    print(f"average: {total / TRIALS}")
