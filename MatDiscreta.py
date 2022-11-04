import time


def main():
    A = [1,2,3,4,5]

    ini = time.time()
    Classificador(A)
    fim = time.time()
    with open('5elementos.txt', 'a') as arquivo:
        arquivo.write(str(' Tempo: '))
        arquivo.write(str(fim - ini))


def ProdCart(a, b):
    c = []
    for i in range(len(a)):
        for j in range(len(b)):
            c.append((a[i], b[j]))
    return c


def PartesDe(a):
    resultado = [[]]
    for i in a:
        resultado += [sub + [i] for sub in resultado]
    return resultado


def Reflexiva(rel, A):
    for i in A:
        if not (i, i) in rel:
            return " "
    return "R"


def Simetrica(rel, A):
    for i in A:
        for j in A:
            if (i, j) in rel and not (j, i) in rel:
                return " "
    return "S"


def Transitiva(rel, A):
    for i in A:
        for j in A:
            for k in A:
                if (i, j) in rel and (j, k) in rel and not (i, k) in rel:
                    return " "
    return "T"


def Classifica(rel, A):
    S = Reflexiva(rel, A) + Transitiva(rel, A) + Simetrica(rel, A)

    if S == "RTS":
        S += "E"
    return S


def Classificador(A):
    for rel in PartesDe(ProdCart(A, A)):
        with open('5elementos.txt', 'a') as arquivo:
            arquivo.write(str(Classifica(rel, A)) + '\n')


if __name__ == "__main__":
    main()
