
# Triangle
'''
    link: https://www.codingninjas.com/studio/problems/triangle_6573690
'''


def triangle( n:int) ->None:

    # To create a row
    for i in range(1,n+1):

        # To generate series in row
        for j in range(i):
            print(i,end=' ')
        
        print()