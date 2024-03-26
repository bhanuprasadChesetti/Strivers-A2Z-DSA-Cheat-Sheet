

# Check Prime
'''
    link: https://www.codingninjas.com/studio/problems/check-prime_624934
'''


from math import *
from collections import *
from sys import *
from os import *



def check_prime(number:int)->bool:

    '''
        Logic:  
            If number > 1 &  there exist a factor betwen 2 and sqrt(number), 
            then it is non-prime.
    '''


    if (number <= 1):
        return False
        

    limit = ceil(sqrt(number)) + 1

    for i in range(2, limit):

        if ( number % i == 0 ):
            return False

    return True
    

n = int(input())
print('YES' if check_prime(n) else 'NO')