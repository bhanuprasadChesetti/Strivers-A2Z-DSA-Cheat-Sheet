
# Ninja And The Number Pattern
'''
    link: https://www.codingninjas.com/studio/problems/ninja-and-the-number-pattern-i_6581959
'''


def getNumberPattern(n):


    '''
        # Approach:
        ----------

        For input n = 4,

        We need to print the following:
            4 <- Outer rectangle
            3 <- Inner rectangle inside of 4
            2 <- Inner rectangle inside of 3
            1 <- Inner rectangel inside of 2.


        Let us take below are the generated pairs, for input 4.

        ( 3,-3) ( 3,-2) ( 3,-1) ( 3,0) ( 3,1) ( 3,2) ( 3,3) 
        ( 2,-3) ( 2,-2) ( 2,-1) ( 2,0) ( 2,1) ( 2,2) ( 2,3) 
        ( 1,-3) ( 1,-2) ( 1,-1) ( 1,0) ( 1,1) ( 1,2) ( 1,3) 
        ( 0,-3) ( 0,-2) ( 0,-1) ( 0,0) ( 0,1) ( 0,2) ( 0,3) 
        (-1,-3) (-1,-2) (-1,-1) (-1,0) (-1,1) (-1,2) (-1,3) 
        (-2,-3) (-2,-2) (-2,-1) (-2,0) (-2,1) (-2,2) (-2,3) 
        (-3,-3) (-3,-2) (-3,-1) (-3,0) (-3,1) (-3,2) (-3,3)


            
        The positions where we print 4 are:

             Location    |  Paris are  
           ---------------------------
            First row    |  ( 3,x)   
            Last  row    |  (-3,x)
            First column |  (x,-3)
            Last  column |  (x, 3)

        Note: (x can be any other number)

        Here,the common logic for all possible pairs that prints 4 as the output is,
        the maximum value in the pair of abs(x) and abs(y) is 3.

        i,e for pair 3,-2
        
            => absolute value of 3  = 3
            => absolute value of -2 = 2

            Now, maximum of (3,2) is 3.

        

        Similarly, for other outputs

            Output  | max(abs(x),abs(y)) 
           -------------------------------
               4    |        3
               3    |        2
               2    |        1
               1    |        0
    '''

    for i in range((n-1),-n,-1):

        for j in range(-(n-1),n,1):

            dominant_coordinate = max(abs(i),abs(j))

            print(dominant_coordinate+1,end='')

        print()

