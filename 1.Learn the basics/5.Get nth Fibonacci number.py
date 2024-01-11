


# Finding nth fibonacci number
'''
    link: https://www.codingninjas.com/studio/problems/nth-fibonacci-number_74156
'''



# Get nth fibonacci
def get_fibonacci_number(
    required_fibonacci_no,
    first = 1,
    second = 1
):
    
    if required_fibonacci_no == 1: # 1st fibonacci number
        return first
    elif required_fibonacci_no == 2: # 2nd fibonacci number
        return second

    
    a = first
    b = second

    for _ in range(2,required_fibonacci_no):
        a,b = b,a+b
    
    return b
    



# Reading which fibonacci number is required
required_fibonacci_no = int(input())

print(get_fibonacci_number(required_fibonacci_no))
