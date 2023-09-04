from my_module import is_prime

primes = []
for x in range(1000000):
    if is_prime(x):
        primes.append(x)

longest_len = 1
longest_sum = 2
n = len(primes)
start_idx = 0
while (True):
    if start_idx > n - longest_len:
        break
    cur_sum = 0
    for i in range(start_idx, n):
        cur_sum += primes[i]
        if cur_sum >= 1000000:
            break
        if is_prime(cur_sum) and (i-start_idx+1) > longest_len:
            longest_len = i - start_idx + 1
            longest_sum = cur_sum
    start_idx += 1

print(longest_sum)
