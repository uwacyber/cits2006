import hashlib
import random
import string

# Preimage resistance: for a given hash value h, it is hard to find any message x with H(x) = h.
# We only compare the first few hex digits of MD5. Make HASH_VALUE longer to see how much harder
# it gets: each extra hex digit is 4 more bits, so about 16 times more tries.
HASH_VALUE = 'b86d'
TRIALS = 20  # increase for a better average
ALPHABET = string.ascii_letters + string.digits + string.punctuation


def random_message(length=16):
    return ''.join(random.choice(ALPHABET) for _ in range(length))


def tries_to_match(prefix):
    """Hash random messages until one's MD5 hex digest starts with prefix; return the number of tries."""
    tried = 0
    while True:
        tried += 1
        if hashlib.md5(random_message().encode()).hexdigest().startswith(prefix):
            return tried


if __name__ == '__main__':
    total = 0
    for i in range(TRIALS):
        tried = tries_to_match(HASH_VALUE)
        print(f"run {i+1}: {tried}")
        total += tried
    print(f"average: {total / TRIALS}")
