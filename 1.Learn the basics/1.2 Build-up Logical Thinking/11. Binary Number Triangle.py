

# Binary Number Triangel
'''
    link: https://www.codingninjas.com/studio/problems/binary-number-triangle_6581890
'''


def nBinaryTriangle(n: int) -> None:

    '''
        Pattern:
        -------
            1 
            0 1 
            1 0 1 
            0 1 0 1 
            1 0 1 0 1 
            0 1 0 1 0 1

        
        Logic:
        ------
            -> We need either 0 or 1 as value, it can be achieved with modulus division by 2.
               
                 i,e by dividing with 2 we will get remainder as 0 or 1.
            
                if dividend is odd  --> Remainder is 1
                            is even --> Remainder is 0.

            -> So, by using row number & column number of value we can get that.
            
                Ex. for printing 5th row

                    i's value is 4
                    j's value starts from 1 to 6

                    Now, values of row as follows

                    1st : (4+1)%2 = (odd)%2  =  1
                    2nd : (4+2)%2 = (even)%2 =  0
                    3rd : (4+3)%2 = (odd)%2  =  1
                    4th : (4+4)%2 = (even)%2 =  0
                    5th : (4+5)%2 = (odd)%2  =  1


    '''


    for i in range(0,n):
        for j in range(1,i+2):
            print((i+j)%2,end=" ")
        
        print()


nBinaryTriangle(3)
