

# Number Crown
'''
    link: https://www.codingninjas.com/studio/problems/number-crown_6581894
'''


def numberCrown(n: int) -> None:


    # Iterate over each row
    for i in range(1,n+1):

        '''
            For each row we print 'i' numbers and left with 'n-i' numbers in one half of the crown,
            and for each number, we should print 'number+space'.

            Ex: for row 2 with n = 8.

                '1 2                         2 1 '
                     <----------------------> 
                     (8-2) = 6 numbers on side.
                     Total 12 numbers in a row.
                     we should print no+space,
                     so, (8-2)*2*2 = 24 spaces
                      
        '''                         
        no_of_spaces = (n-i)*4

        forward_series = ''
        backward_series = ''

        for j in range(1,i+1):
            forward_series  = forward_series + f'{j} '
            backward_series = f'{j} ' + backward_series


        print(f'{forward_series}{no_of_spaces*" "}{backward_series}')


numberCrown(9)
        
