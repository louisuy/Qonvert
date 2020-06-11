import math

def julian_to_jd(*args):
    Y = 2020
    M = 2
    D = 10

    if Y < 1:
        Y+= 1

    if M <= 2:
        Y-= 1
        M+= 12

    return((math.floor((365.25 * (Y + 4716))) + math.floor((30.6001 * (M + 1))) + D) - 1524.5)

print(julian_to_jd())