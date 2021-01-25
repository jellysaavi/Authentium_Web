import logging
from random import randint
import random
import re
import string

from django.core.exceptions import ValidationError
from django.core.validators import validate_ipv46_address

logger = logging.getLogger(__name__)


#  ---------------------------------------------------------------
# generate_code
#  ---------------------------------------------------------------
def generate_code(length=4):
    """
    Generate random digits.
    """
    
    return ''.join(
        random.choice(re.sub("[0]", "", string.digits)) for _ in range(4)
    )    


#  ---------------------------------------------------------------
# random_digits
#  ---------------------------------------------------------------
def random_digits(n=10):
    """
    Generate random digits.
    """
    
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end) 


# ---------------------------------------------------------------------------
# randomStringDigits
# ---------------------------------------------------------------------------
def randomStringDigits(stringLength=6):
    """
    Generate a random string of letters and digits 
    """
    
    lettersAndDigits = string.ascii_letters + string.digits
    return ''.join(random.choice(lettersAndDigits) for i in range(stringLength))
