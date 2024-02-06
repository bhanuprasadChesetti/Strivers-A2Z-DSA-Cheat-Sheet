
# Seeding
'''
    link: https://www.codingninjas.com/studio/problems/seeding_6581892
'''


def seeding(n: int) -> None:

    # To iterate row wise
    for i in range(n,0,-1):

        # Row logic
        for j in range(i):
            print('*',end=' ')

        print()

seeding(4)