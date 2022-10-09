# ndig ⇐ 1 + max( 0, ⌊log(x)/log(n)⌋ )
# para i ⇐ ( ndig - 1 ) .. 0:
#   p ⇐ n ^ i
#   d ⇐ ⌊x/p⌋
#   x ⇐ x mod p
#   apresenta d

from math import log2
from math import floor


def main():
    n = int(input("Digite sua base : "))
    x = int(input("Digite seu número em decimal: "))

    if n > 1 and x > 0:
        Bases(n, x)
    else:
        print("Siga: (Base > 1) e (Número > 0)")


def Bases(n, x):
    nu = x
    lista = []
    ndig = 1 + max(0, floor(log2(x) / log2(n)))
    i = ndig - 1

    while i >= 0:
        p = n ** i
        d = floor(x / p)
        x = x % p
        i -= 1
        lista.append(d)

    print()
    print("{} na base {} é: ".format(nu, n), end="")
    for i in lista:
        print(i, end="")


if __name__ == "__main__":
    main()
