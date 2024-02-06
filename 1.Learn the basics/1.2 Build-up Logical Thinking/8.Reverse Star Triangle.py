

# Reverse Star Triangle
'''
    link: https://www.codingninjas.com/studio/problems/reverse-star-triangle_6573685
'''

def nStarTriangle(n: int) -> None:

    for i in range(n,0,-1):

        # ** Row logic **

        no_of_spaces = n-i

        '''      
            we need odd number of stars
            for getting kth odd number : 2(k-1)+1
        '''
        no_of_stars = 2*(i-1) + 1


        print(f"{' '*no_of_spaces}{'*'*no_of_stars}{' '*no_of_spaces}")



nStarTriangle(5)