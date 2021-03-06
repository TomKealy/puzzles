from fractions import gcd

def primitive_roots(prime):
    primitive_roots = []
    num_to_check = 0
    for each in range(1, prime):
	num_to_check += 1
        candidate_prim_roots = []
        for i in range(1, prime):
            modulus = (num_to_check ** i) % prime
            candidate_prim_roots.append(modulus)
            cleanedup_candidate_prim_roots = set(candidate_prim_roots)
            if len(cleanedup_candidate_prim_roots) == len(range(1,prime)):
                primitive_roots.append(num_to_check)
    return primitive_roots

def sundaram3(max_n):
    numbers = range(3, max_n+1, 2)
    half = (max_n)//2
    initial = 4

    for step in xrange(3, max_n+1, 2):
        for i in xrange(initial, half, step):
            numbers[i-1] = 0
        initial += 2*(step+1)

        if initial > half:
            return [2] + filter(None, numbers)

primes = sundaram3(1000)
filtered = []
for p in primes:
    if gcd(p, 10) == 1:
        filtered.append(p)
