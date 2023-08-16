#Triangle	 	Tn=n(n+1)/2	 	1, 3, 6, 10, 15, ...
#Pentagonal	 	Pn=n(3n−1)/2	1, 5, 12, 22, 35, ...
#Hexagonal	 	Hn=n(2n−1)	 	1, 6, 15, 28, 45, ...
#It can be verified that T285 = P165 = H143 = 40755.
#Find the next triangle number that is also pentagonal and hexagonal.

def computeT(i):
    return i * (i+1) / 2

def computeP(i):
    return i * (3 * i - 1) / 2

def computeH(i):
    return i * (2 * i - 1)

t = computeT(286)
ti = 286
p = computeP(166)
pi = 166
h = computeH(144)
hi = 144

idx = 0
while(not (t == p == h)):
    if (t <= p and t <= h):
        ti += 1
        t = computeT(ti)
    elif (p <= t and p <= h):
        pi += 1
        p = computeP(pi)
    else:
        hi += 1
        h = computeH(hi)
    idx += 1
    if idx == 1000000:
        break

print(t, p, h)