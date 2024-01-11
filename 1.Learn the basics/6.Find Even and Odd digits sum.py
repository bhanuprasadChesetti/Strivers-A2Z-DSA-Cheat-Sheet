

# Finding even and odd digits sum in a number
'''
    link: https://www.codingninjas.com/studio/problems/sum-of-even-odd_624650
'''




# Get Sum of even and odd digits
def get_sum_of_even_and_odd_digits(
    number
):
    '''
        Returns the even and odd digits sum.

        args:
            - number : Any positive number

        returns: (even digits sum, odd digits sum)
        
    '''

    even_digits_sum:int = 0
    
    odd_digits_sum:int = 0


    while(number):

        # Getting the right most digit in the nubmer
        digit = number%10

        
        # Checking even or odd
        if (digit % 2 == 0):
            even_digits_sum += digit
        else:
            odd_digits_sum += digit


        # Updating the number
        number = (number-digit)//10

    
    return (
        even_digits_sum,
        odd_digits_sum
    )


number = int(input())

even_digits_sum,odd_digits_sum = get_sum_of_even_and_odd_digits(number)

print(f'{even_digits_sum} {odd_digits_sum}')

