from my_module import permutation
'''
for x in 1000 to 9999:
    if x not in seen:
        get all permutations of x's digits
        add them to seen
        filter out perms that are not prime
        get all choose 3 from prime perms
        order them and check if they form an arithm seq
'''

seen = set()
for x in range(1000, 10000):
    digits_x = sorted(str(x))
    hash_x = int(''.join(digits_x))
    if hash_x not in seen:
        seen.add(hash_x)
        perms = permutation(digits_x)
        
