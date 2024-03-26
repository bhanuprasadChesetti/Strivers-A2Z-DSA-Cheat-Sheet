
# Check Armstrong
'''
    link: https://www.codingninjas.com/studio/problems/check-armstrong_589
'''



from os import *
from sys import *
from collections import *
from math import *



def check_armstrong(number:int)->bool:

    orginal_number = number

    length = len(str(orginal_number))

    sum_of_power_of_digit_with_length = 0

    while (number != 0):
        
        right_most_digit = number % 10

        sum_of_power_of_digit_with_length += (right_most_digit ** length)

        number = number // 10


    return 'true' if (orginal_number == sum_of_power_of_digit_with_length) else 'false'



n = int(input())
print(check_armstrong(n))



