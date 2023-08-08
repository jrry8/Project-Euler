# find the l = longest length word in words.txt
# max word value = 26 * l
# create hash table of all triangle numbers <= max word value
# iterate over every word in words.txt and check if it is triangle word

# iterate over every word in words.txt:
    # find v = word value
    # compute n = floor(sqrt(2v))
    # check if 2v == n(n+1)

import math

with open("C:/Users/xujer/OneDrive/Coding practice/Project Euler/p042_words.txt", "r") as f:
    contents = f.read()
    clean = contents.replace('"', '')
    names = clean.split(",")

triangleWords = 0
for name in names:
    v = 0
    for letter in name:
        v += ord(letter) - 64
    n = math.floor(math.sqrt(2 * v))
    if 2 * v == n * (n + 1):
        triangleWords += 1
print(triangleWords)


