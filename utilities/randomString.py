#Generating random data such as email

import random
import string
from random import choice
from string import ascii_lowercase


def random_string_generator(size=5,chars=string+ascii_lowercase +string.digits):
    return ''.join(random.choice(chars) for x in range(size))