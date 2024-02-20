

# Ninja And The Star Pattern I
'''
    link: https://www.codingninjas.com/studio/problems/ninja-and-the-star-pattern-i_6581920
'''


def getStarPattern(n: int) -> None:

    if (n==1):
        print('*')
    else:

        # First row
        print('*'*n)


        no_of_spaces = n-2

        for _ in range(n-2):
            print(f"*{ ' ' * no_of_spaces}*")


        # Last row
        print('*'*n)


