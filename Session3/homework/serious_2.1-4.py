flock = [6, 50, 74, 210, 104, 17, 133]
print("My name is Giang and these are my ship sizes: ", flock)
print()

biggest = max(flock)
print("Now my biggest sheep has size", biggest, ", let's shear it")
print()

poor_sheep = flock.index(biggest)
flock[poor_sheep] = 8
print("After shearing it, here is my new flock", flock, sep = "\n")

pos = 0
for pos in range(len(flock)):
    flock[pos] = flock[pos] + 50
    pos += 1
print('One month has passed, here is my new flock', flock, sep ="\n")
