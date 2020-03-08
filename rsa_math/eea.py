def EEA(a, b):
    """
    Source: https://en.wikibooks.org/wiki/Algorithm_Implementation/Mathematics/Extended_Euclidean_algorithm
    Extended Euclidean Algorithm (EEA)
    Parameters: Positive integers a and b whereby a > b
    Returns: ( gcd(a,b), s, t )  such that gcd(a,b) = s*a + t*b
    """
    assert a > b
    x0, x1, y0, y1 = 1, 0, 0, 1
    while a != 0:
        q, b, a = b // a, a, b % a
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return  b, y0, x0