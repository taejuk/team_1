import random
from math import ceil
from decimal import *

global field_size
field_size = 10**5


def reconstructSecret(shares):

    sums, prod_arr = 0, []

    for j in range(len(shares)):
        xj, yj = shares[j][0], shares[j][1]
        prod = Decimal(1)

        for i in range(len(shares)):
            xi = shares[i][0]
            if i != j:
                # x=0일 때, secret값이 반환된다. 이 사실을 잘 알아야 함.
                prod *= Decimal(Decimal(xi)/(xi-xj))

        prod *= yj
        sums += Decimal(prod)
    return int(round(Decimal(sums), 0))


def polynom(x, coeff):
    return sum([x**(len(coeff)-i-1) * coeff[i] for i in range(len(coeff))])


def coeff(t, secret):

    coeff = [random.randrange(0, field_size) for _ in range(t-1)]
    coeff.append(secret)

    return coeff


def generateShares(n, m, secret):

    cfs = coeff(m, secret)
    shares = []

    for i in range(1, n+1):
        r = random.randrange(1, field_size)
        shares.append([r, polynom(r, cfs)])

    return shares


def start(t0, n0, private_key):
    # (3,5) sharing scheme
    t = t0
    n = n0
    secret = private_key

    # Phase I: Generation of shares
    shares = generateShares(n, t, secret)

    # Phase II: Secret Reconstruction
    # Picking t shares randomly for
    # reconstruction
    pool = random.sample(shares, t)
    return reconstructSecret(pool)
