import math, random
from rsa_math import eea, primes

class RSA:
    def generate_keys(n=512):
        p, q = primes.generate(n=n, k=2)
        n = p*q
        phi = (p-1)*(q-1)

        while True:
            e = random.randrange(1, phi-1)
            if math.gcd(e, phi) == 1:
                gcd, s, t = eea.EEA(phi, e)
                if gcd == (s*phi + t*e):
                    d = t % phi
                    break
        return ((e, n),(d, n))
