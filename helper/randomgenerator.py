import random
import string

def generate_random_email():
    """Generate a random email address with yopmail.com"""
    length = random.randint(6, 12)  # Random length between 6 and 12 characters
    random_string = ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))
    return f"{random_string}@yopmail.com"

def generate_phone():
    """Generate a random Indonesian phone number"""
    phone_prefix = "0813"
    random_digits = ''.join(random.choices(string.digits, k=9))  # Random 9 digits
    return phone_prefix + random_digits
