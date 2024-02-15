

# Increasing Number Triangel
'''
    link: https://www.codingninjas.com/studio/problems/increasing-number-triangle_6581893
'''


def nNumberTriangle(n: int) -> None:

    next_value_in_series = 0

    for i in range(1,n+1):
        for j in range(i):
            next_value_in_series += 1
            print(next_value_in_series,end=' ')
        print()
        

nNumberTriangle(7)