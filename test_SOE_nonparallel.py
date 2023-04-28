def scanIfDivisible(scanList, curPrime):
    trimNumlist = []

    for x in scanList:
        if x % curPrime != 0:
            trimNumlist.append(x)
    
    return trimNumlist

def sieveOfEratosthenes(N):
    primeList = list(range(2,N+1))
    print(f'{primeList}\n')

    i = 0
    x = primeList[i]
    
    while x**2 <= N:    
        scanList = primeList[i+1:]
        trimNumList = scanIfDivisible(scanList, x)
        primeList = primeList[:i+1] + trimNumList
        print(f'cur Prime:{x} \n{primeList}\n')

        i+=1
        x = primeList[i]
        


    return primeList


N = int(input('gib num: '))

primes = sieveOfEratosthenes(N)

print(f'Answer:\n{primes}')