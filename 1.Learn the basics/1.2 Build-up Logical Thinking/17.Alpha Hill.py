

# Alpha Hill
'''
    link: https://www.codingninjas.com/studio/problems/alpha-hill_6581921
'''



def alphaHill(n: int):

    for i in range(n):

        # As each row starts with 'A'
        next_letter_in_series = 64


        # To print forward & backward series 
        step = 1



        no_of_spaces = (n-1-i)*2


        print(' '*no_of_spaces ,end='')


        '''
            For every row, we need to print odd number of values
            i,e for 3rd row, number of alaphabets are 3rd odd number (2*(3-1)+1 = 5)
        '''
        for j in range(2*i+1):

            next_letter_in_series += step

            print(chr(next_letter_in_series),end=' ')


            # To print right half of the row, we should decrease the step
            if (next_letter_in_series == (65+i)):
                step = -1
        
        print(' '*no_of_spaces)


alphaHill(9)