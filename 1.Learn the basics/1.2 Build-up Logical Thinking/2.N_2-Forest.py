

# N/2 Forest
'''
    link: https://www.codingninjas.com/studio/problems/n-2-forest_6570178
'''


def nForest(n:int) ->None:

    # To iterate on each row
    for i in range(1,n+1):

        # To print stars in a row
        for _ in range(i):
            print('* ',end=' ')

        
        # To move the cursor to new line
        print('\n')