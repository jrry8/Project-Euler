import time

start_time = time.perf_counter()
num = 28433
for _ in range(7830457):
    num *= 2
    num %= 10000000000
num += 1
num %= 10000000000
end_time = time.perf_counter()
print(num)
print(f'Runtime: {end_time-start_time:0.2f}s')