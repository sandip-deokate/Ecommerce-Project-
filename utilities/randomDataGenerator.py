import random
import string
import numbers

def ramdom_Email_Generator(size=5,char=string.ascii_lowercase + string.digits):
    return "".join(random.choice(char) for x in range(size))

