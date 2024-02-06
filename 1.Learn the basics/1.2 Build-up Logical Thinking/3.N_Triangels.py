
# N-Triangles
'''
    link: https://www.codingninjas.com/studio/problems/n-triangles_6573689
'''


def nTriangle(n:int) ->None:
    
    # To iterate on rows
    for i in range(1,n+1):

        # To generate series in rows
        for j in range(1,i+1):
            print(j,end=" ")

        print()


nTriangle(3)