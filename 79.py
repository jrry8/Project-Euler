# construct DAG

logins = []
with open("0079_keylog.txt") as f:
    for line in f:
        logins.append([line[0], line[1]])
        logins.append([line[1], line[2]])

print(logins)