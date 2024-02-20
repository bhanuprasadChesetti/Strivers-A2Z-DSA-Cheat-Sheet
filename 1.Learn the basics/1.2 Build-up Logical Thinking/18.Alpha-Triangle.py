

# Alpha-Triangle
'''
    link: https://www.codingninjas.com/studio/problems/alpha-triangle_6581429
'''


def alphaTriangle(n: int):

    for i in range(1,n+1):

        # Each row starts with alphabet corresponds to ASCII value of '64+n'
        next_letter_in_series = 64+n

        for j in range(i):
            
            print(chr(next_letter_in_series),end=' ')

            next_letter_in_series -= 1
        
        print()



