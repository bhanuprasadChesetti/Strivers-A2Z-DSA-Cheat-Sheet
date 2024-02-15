


# Reverse Letter Triangle
'''
    link: https://www.codingninjas.com/studio/problems/increasing-letter-triangle_6581897
'''



def nLetterTriangle(n: int):

   
    for i in range(n,0,-1):

        # ASCII value of 'A' starts with 65, so initalized it with 64.
        next_letter_in_series = 64

        for j in range(i):

            next_letter_in_series += 1

            print(chr(next_letter_in_series),end=' ')

        print()

