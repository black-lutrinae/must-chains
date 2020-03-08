import re
import random
import math

def fermat_primality_test(p, s=5):
    """
    a^(p-1) ≡ 1 mod p
    Input: prime candidate p and security paramter s
    Output: either p is a composite (always trues), or
            p is a prime (with probability)
    """
    if p == 2:
        return True
    if not p & 1:
        return False

    for i in range(s):
        a = random.randrange(2, p-2)
        x = pow(a, p-1, p)
        if x != 1:
            return False
    return True

def square_and_multiply(x, k, p=None):
    """
    Square and Multiply Algorithm
    Parameters: positive integer x and integer exponent k,
                optional modulus p
    Returns: x**k or x**k mod p when p is given
    """
    b = bin(k).lstrip('0b')
    r = 1
    for i in b:
        r = r**2
        if i == '1':
            r = r * x
        if p:
            r %= p
    return r

def miller_rabin_primality_test(p, s=5):
    if p == 2:
        return True
    if not (p & 1):
        return False

    p1 = p - 1
    u = 0
    r = p1

    while r % 2 == 0:
        r >>= 1
        u += 1

    assert p-1 == 2**u * r

    def witness(a):
        """
        Returns: True, if there is a witness that p is not prime.
                 False, when p might be prime
        """
        z = square_and_multiply(a, r, p)
        if z == 1:
            return False

        for i in range(u):
            z = square_and_multiply(a, 2**i * r, p)
            if z == p1:
                return False
        return True

    for j in range(s):
        a = random.randrange(2, p-2)
        if witness(a):
            return False

    return True

def generate(n=512, k=1):
    """
    Generates prime numbers with bitlength n.
    Stops after the generation of k prime numbers.
    """
    assert k > 0
    assert n > 0 and n < 4096

    necessary_steps = math.floor( math.log(2**n) / 2 )
    x = random.getrandbits(n)

    primes = []

    while k>0:
        if miller_rabin_primality_test(x, s=7):
            primes.append(x)
            k = k-1
        x = x+1

    return primes