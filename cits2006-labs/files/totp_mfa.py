import hmac
import hashlib
from time import time


def get_hotp_token(secret: str, intervals_no: int) -> int:
    '''Generate a HMAC-based One-Time Password (HOTP)'''
    secret = secret.encode('utf-8')
    print(type(secret))
    msg = int.to_bytes(intervals_no, 8, 'big')
    hmac_digest = hmac.new(secret, msg, hashlib.sha1).digest()
    otp = (int.from_bytes(hmac_digest[:4], 'big') & 0xffffffff) % 1000000
    return otp

def get_totp_token(secret: str) -> int:
    '''Generate a Time-based One-Time Password (TOTP)'''
    return get_hotp_token(secret, intervals_no=int(time()))

def verify_totp(token: int, secret: str, window: int = 10) -> bool:
    '''Verify a TOTP given a specific window
       default time set to 10 seconds'''
    # YOUR CODE GOES HERE
    return True


# Test the MFA process
if __name__ == '__main__':
    password = input("enter your password: ")

    totp_token = get_totp_token(password)
    print('TOTP Token:', totp_token)

    # Simulate user input or API call
    entered_password = int(input('Enter the TOTP token displayed on your authenticator (within 10 seconds!): '))

    if verify_totp(entered_password, password):
        print('Authentication successful!')
    else:
        print('Authentication failed. Please try again.')

