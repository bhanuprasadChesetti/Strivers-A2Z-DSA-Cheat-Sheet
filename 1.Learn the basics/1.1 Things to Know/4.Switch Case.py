from typing import *
import math

def areaSwitchCase(ch: int, a: List[float]):

    area : float = 0


    # Calculating area based on shape
    match ch:
        case 1: # Circle
            area =  math.pi * a[0] * a[0]
        case 2: # Rectangle
            area = a[0] * a[1]

    # Rounding the area upto 5 decimals
    area =  format(area,'.5f')

    return area
    