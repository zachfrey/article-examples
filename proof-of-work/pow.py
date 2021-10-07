import hashlib

poem = open("proof-of-work\\the-road-not-taken.txt", "r")

lines = poem.readlines()

for line in lines:
    l = line.strip()
    print(l, hashlib.sha256(l.encode()).hexdigest())

poem.close()
