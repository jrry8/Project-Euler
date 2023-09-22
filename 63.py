import time

start_time = time.perf_counter()
count = 0
n = 1
while True:
    tmp = 9 ** n
    if len(str(tmp)) < n:
        break
    for i in range(1, 10):
        tmp = i ** n
        if len(str(tmp)) == n:
            count += 1
    n += 1
end_time = time.perf_counter()

print(count)
print(f'Runtime: {end_time-start_time:0.2f}s')
