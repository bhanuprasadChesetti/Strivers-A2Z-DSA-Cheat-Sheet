


# Star Triangle
'''
    link: https://www.codingninjas.com/studio/problems/star-triangle_6573671
'''


def nStarTriangle(n: int) -> None:

    # initial declaration 
    no_of_stars = -1

    for i in range(1,n+1):

        # ** Row logic **

        no_of_spaces = n-i
        no_of_stars += 2

        print(f"{' ' * no_of_spaces}{'*' * no_of_stars}")


nStarTriangle(10)