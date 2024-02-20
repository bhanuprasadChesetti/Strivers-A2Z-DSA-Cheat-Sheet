

# Symmetry
'''
    link: https://www.codingninjas.com/studio/problems/symmetry_6581914
'''



def symmetry(n: int):

    max_number_of_stars_in_a_row = 2*n

    for i in range(2*n-1):

        if (i < n):
            # logic for first n rows
            
            no_of_stars_in_one_half = i + 1

            no_of_spaces = (max_number_of_stars_in_a_row - (no_of_stars_in_one_half * 2))*2 # we print 2 spaces
        else:
            # logic for remaining n rows
            
            no_of_stars_in_one_half = (n-1) - (i%n)

            no_of_spaces = (max_number_of_stars_in_a_row - (no_of_stars_in_one_half * 2))*2 # we print 2 spaces

    
        print(f"{'* ' * no_of_stars_in_one_half}{' ' * no_of_spaces}{'* ' * no_of_stars_in_one_half}")


