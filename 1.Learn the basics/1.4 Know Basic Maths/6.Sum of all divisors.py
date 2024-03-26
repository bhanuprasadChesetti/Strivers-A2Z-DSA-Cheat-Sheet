

# Sum of all divisors
'''
    link: https://www.codingninjas.com/studio/problems/sum-of-all-divisors_8360720
'''

def sumOfAllDivisors(n: int) -> int:


    def get_sum_of_divisiors(number: int)->int:

        sum_of_divisiors = number

        # No divisior exists after the number n//2 except n
        limit = (number // 2) + 1

        for i in range(1,limit):
            if (number%i == 0):
                sum_of_divisiors += i

        return sum_of_divisiors

    
    sum_of_all_divisiors = 0

    for i in range(1,n+1):
        sum_of_all_divisiors += get_sum_of_divisiors(i)

    return sum_of_all_divisiors


n = int(input())
print(sumOfAllDivisors(n))

