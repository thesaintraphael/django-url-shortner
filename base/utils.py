import string
import random
from . import models


def generate_unique_code():
    length = 6

    while True:
        code = ''.join(random.choices(string.ascii_uppercase, k=length))
        if not models.Link.objects.filter(code=code).exists():
            break

    return code
