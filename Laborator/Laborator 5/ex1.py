seed = int(input("Introduceti seed "))

# Candidate 1
try:
    while True:
        print(seed)
        seed = seed ^ seed
except KeyboardInterrupt:
    pass

# Candidate 2
try:
    while True:
        print(seed)
        seed = int(seed + seed / 2)
except KeyboardInterrupt:
    pass

# Candidate 3
print(seed>>2)