
#  GCD or HCF
'''
    link: https://www.codingninjas.com/studio/problems/hcf-and-lcm_840448
'''


def calcGDC(m:int, n: int) -> int:
    while m!=0:
        m,n = n%m,m

    return n



