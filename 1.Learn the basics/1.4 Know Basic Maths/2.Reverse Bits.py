
# Reverse Bits
'''
    link: https://www.codingninjas.com/studio/problems/reverse-bits_2181102
'''


def reverseBits(n):

    # For a 32 bit unsigned integer 2's power are from 0-31
    # After reversing every LSB bit of the number, is multipled with the power 32 - kth bit.
    power_starts_with = 31

    reverse_number = 0

    while (n):

        remainder = n%2

        if remainder == 1:
            reverse_number += (2**power_starts_with)

        power_starts_with -= 1
        n = n//2

    return reverse_number


