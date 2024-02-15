

# Alpha-Ramp
'''
    link: https://www.codingninjas.com/studio/problems/alpha-ramp_6581888
'''


def alphaRamp(n: int) -> None:

    corresponding_row_letter = 64

    for i in range(1,n+1):

        corresponding_row_letter += 1

        row = f'{chr(corresponding_row_letter)} '*i

        print(row)
