flock = [6, 50, 74, 210, 104, 17, 133]
m = int(input('How many months? '))

for i in range(1, m+1):
    pos = 0
    for pos in range(len(flock)):
        flock[pos] = flock[pos] + 50
        pos += 1
    print("Month", i)
    print('One month has passed, here is my new flock', flock, sep ="\n")
    
    biggest = max(flock)
    print("Now my biggest sheep has size", biggest, ", let's shear it")
    
    poor_sheep = flock.index(biggest)
    flock[poor_sheep] = 8
    print("After shearing it, here is my new flock", flock, sep = "\n")
    print()