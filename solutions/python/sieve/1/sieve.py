def primes(limit):
    prime = [True for i in range(limit+1)]
    prime_list = []
    p = 2

    while(p**2 <= limit):
        if prime[p] == True:
            for i in range(p*2, limit+1, p):
                prime[i] = False
        p += 1
    
    for p in range(2, limit+1):
        if prime[p]:
            prime_list.append(p)

    return prime_list
