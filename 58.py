import time

import my_module


start_time = time.perf_counter()

cur = 1
prime_elems = 0.0
num_layers = 0
while True:
    num_layers += 1
    # check each corner element (i.e. on the diagonal) in this layer if it is prime
    for _ in range(4):
        cur += 2 * num_layers
        if my_module.is_prime(cur):
            prime_elems += 1
    diag_elems = 4*num_layers + 1
    # check if ratio has fallen below 10%
    if (prime_elems / diag_elems) < 0.1:
        break
    if time.perf_counter() - start_time > 60:
        print('Max runtime reached. Terminated early.')
        break

print(prime_elems, diag_elems, prime_elems / diag_elems)
print(num_layers*2 + 1)

end_time = time.perf_counter()
print(f'Runtime: {end_time-start_time:0.2f}s')
