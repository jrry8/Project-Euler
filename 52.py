for x in range(1, 1000000):
    tmp = sorted(str(x))
    success = True
    for m in range(2, 7):
        if sorted(str(m * x)) != tmp:
            success = False
            break
    if success:
        for i in range(7):
            print(i * x)
        break

