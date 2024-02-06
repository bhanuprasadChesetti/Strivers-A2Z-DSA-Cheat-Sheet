


# Star Diamond
'''
    link: https://www.codingninjas.com/studio/problems/star-diamond_6573686
'''

def nStarDiamond(n: int) -> None:


    '''
        - row_no_with_first_half_ends: Represents the index number where the first half of the diamond ends.
        - For a diamond of size n, the first half ends at row number n-1.
        - This variable is used to determine the number of spaces and stars in each row of the diamond pattern.

        Ex: 

        for a diamond of size 4,
            *   
           ***  
          ***** 
         *******   <-- Here, first half ends.
         *******
          ***** 
           ***  
            *   


    '''
    row_no_with_first_half_ends = n-1


    # we need 2n rows
    for row_no in range(2*n):

        # First Half logic      
        if row_no <= row_no_with_first_half_ends:

            no_of_spaces =  row_no_with_first_half_ends - row_no

            no_of_stars = 2 * row_no + 1 # kth odd number

        # Second Half Logic
        else:
            remainder = (row_no % n)
            no_of_spaces =  remainder
            no_of_stars = 2*(row_no_with_first_half_ends - remainder)+1  # kth odd number


        # Printing the pattern of the row
        print(f"{' '*no_of_spaces}{'*'*no_of_stars}{' '*no_of_spaces}")



nStarDiamond(8)