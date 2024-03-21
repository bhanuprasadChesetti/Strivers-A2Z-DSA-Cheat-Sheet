

# Count Digits
'''
    link: https://www.codingninjas.com/studio/problems/count-digits_8416387
'''


def countDigits(n: int) -> int:
    
    reference_number = n

    no_of_evenly_dividing_digits = 0
    
    while n>0:
        
        # Getting right most digit
        right_most_digit_in_number = n%10

        if (right_most_digit_in_number != 0) and (reference_number % right_most_digit_in_number == 0):
            no_of_evenly_dividing_digits += 1

        n = n // 10

    return no_of_evenly_dividing_digits


while True:
    print(countDigits(int(input("Enter:"))))