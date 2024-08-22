#L3 - Create Python Console Application to randomly generate OTP kind of secure code.

import random           #importing random module
import string           #importing string module

def generate_otp(length):
    letters = string.ascii_letters + string.digits      #stores upper and lower charencters and digits in 'letters' variable
    otp = ''.join(random.choice(letters) for _ in range(length))
    return otp

otp_length = 8
otp = generate_otp(otp_length)
print("Generated OTP:", otp)