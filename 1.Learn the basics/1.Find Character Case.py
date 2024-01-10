

# Finding Character Case
'''
    Link : https://www.codingninjas.com/studio/problems/find-character-case_58513
'''

# Reading the character input
character = input()


# Getting ascii value of entered character
ascii_value_of_character = ord(character)



if (ascii_value_of_character >= 65) and (ascii_value_of_character<=90):
    '''
        ASCII values range of A-Z is 65-90
        So,Character is Upper case alphabet
    '''
    print(1)
elif (ascii_value_of_character >= 97) and (ascii_value_of_character <= 122):
    '''
        ASCII values range of a-z is 97-122
        So,Character is Lower case alphabet
    '''
    print(0)
else:
    '''
        Not an either uppercase or lowercase  alphabet
    '''
    print(-1)