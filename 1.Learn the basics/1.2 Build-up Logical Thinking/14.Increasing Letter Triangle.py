


# Increasing Letter Triangle
'''
    link: https://www.codingninjas.com/studio/problems/increasing-letter-triangle_6581897
'''

def nLetterTriangle(n: int) -> None:
   
    
    
    for i in range(1,n+1):
        
        # ASCII value of 'A' starts with 65, so initalized it with 64.
        next_letter_in_series = 64
        
        for j in range(i):

            next_letter_in_series += 1

            print(chr(next_letter_in_series),end=' ')
        

        print()