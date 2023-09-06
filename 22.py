#parse text file into array
with open(r"0022_names.txt", "r") as f:
    contents = f.read()
    clean = contents.replace('"', '')
    names = clean.split(",")

#helper function for comparing two words based on alphabetical order
#return true if x comes before y
def cmp_words(x: str, y: str) -> bool:
    n = min(len(x), len(y))
    for i in range(n):
        if (x[i] < y[i]):
            return True
        elif (x[i] > y[i]):
            return False
    if (len(x) <= len(y)):
        return True
    return False

#sorting function based on alphabetical order
def quicksort(arr):
    if (len(arr) < 2):
        return arr
    pivot = arr[0]
    pi = 0
    for i in range(1, len(arr)):
        if cmp_words(arr[i], pivot):
            pi += 1
            tmp = arr[i]
            arr[i] = arr[pi]
            arr[pi] = tmp
    tmp = arr[0]
    arr[0] = arr[pi]
    arr[pi] = tmp
    left = quicksort(arr[:pi])
    right = quicksort(arr[pi+1:])
    res = left + [arr[pi]] + right
    return res

#helper function for computing name score
def name_score(x: str) -> int:
    sum = 0
    for c in x:
        sum += ord(c) - 64
    return sum

#sort list, then add up all name scores
names = quicksort(names)
res = 0
for i in range(len(names)):
    res += name_score(names[i]) * (i + 1)
print(res)
