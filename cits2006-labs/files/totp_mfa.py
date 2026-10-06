import base64
import hashlib
import hmac
import os
import struct
import time

TIME_STEP = 30  # seconds per code (RFC 6238 default)
DIGITS = 6


def hotp(secret_b32: str, counter: int, digits: int = DIGITS) -> str:
    """HMAC-based one-time password (RFC 4226) for a counter, as a zero-padded string."""
    key = base64.b32decode(secret_b32.upper() + "=" * (-len(secret_b32) % 8))
    digest = hmac.new(key, struct.pack(">Q", counter), hashlib.sha1).digest()
    offset = digest[-1] & 0x0F                                   # dynamic truncation
    code = int.from_bytes(digest[offset:offset + 4], "big") & 0x7FFFFFFF
    return str(code % 10 ** digits).zfill(digits)


def totp(secret_b32: str, at: float | None = None) -> str:
    """Time-based one-time password (RFC 6238): HOTP with counter = time // 30."""
    now = time.time() if at is None else at
    return hotp(secret_b32, int(now // TIME_STEP))


def verify_totp(code: str, secret_b32: str, window: int = 1, at: float | None = None) -> bool:
    """TASK 2: return True if `code` matches the code for the current time step, or for up to
    `window` steps before or after it (to allow for clock drift and typing time).
    Compare with hmac.compare_digest, not ==."""
    # YOUR CODE GOES HERE
    return True


if __name__ == '__main__':
    secret = base64.b32encode(os.urandom(20)).decode()
    print("Add this account to an authenticator app (enter the key manually):")
    print(f"  key: {secret}")
    print(f"  or URI: otpauth://totp/CITS2006:lab3?secret={secret}&issuer=CITS2006")
    print("Current code from this script:", totp(secret))
    entered = input("Enter the code shown in your authenticator app: ").strip()
    print("Authentication successful!" if verify_totp(entered, secret) else "Authentication failed.")
