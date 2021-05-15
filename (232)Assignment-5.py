primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71]
fakes = []
for i in range(len(primes)-1):
    fakes.append(primes[i] * primes[i+1])

print(fakes)