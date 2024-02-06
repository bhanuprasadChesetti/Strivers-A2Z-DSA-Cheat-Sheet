

# Reverse Number Triangle
'''
    link: https://www.codingninjas.com/studio/problems/reverse-number-triangle_6581889
'''


def nNumberTriangle(n: int) -> None:

    for i in range(n,0,-1):

        # Row logic
        for j in range(1,i+1):
            print(j,end=' ')

        print()