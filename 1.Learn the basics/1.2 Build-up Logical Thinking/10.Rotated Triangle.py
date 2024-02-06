#  Rotated Triangle
'''
    link: https://www.codingninjas.com/studio/problems/rotated-triangle_6573688
'''


def nStarTriangle(n: int) -> None:
    

    no_of_rows = 2 * (n-1) + 1  # nth odd number

    for i in range(1,no_of_rows+1):

        # First Half logic
        if (i <= n):
            no_of_stars = i 
        
        # Second Half Logic 
        else:
            '''
                In second half we needed stars as follows:
                
                1st row     - n-1
                2nd row     - n-2
                ..
                ..
                (n-1)th row - 1
            '''
            no_of_stars = n-(i%n)


        print(f"{'*'*no_of_stars}")


nStarTriangle(21)