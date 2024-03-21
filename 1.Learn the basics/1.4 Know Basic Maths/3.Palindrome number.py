


# Palindrome number
'''
    link: https://www.codingninjas.com/studio/problems/palindrome-number_624662
'''


def check_palindrome_number(number:int):

    orginal_number = number
    reverse_number = 0

    while(number != 0):

        # Getting the right most digit of the number
        right_most_digit = number % 10

        reverse_number = (reverse_number * 10) + right_most_digit

        number = number // 10


    is_palindrome =  True if (orginal_number == reverse_number) else False


    return is_palindrome



n=int(input())  

is_palindrome = check_palindrome_number(n)

print('true') if is_palindrome else print('false')