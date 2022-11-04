import time


def main():
    A = [1, 2, 3, 4, 5,6,7,8,9,0,0]
    if input() == 'M':
        ini = time.time()
        a = len(part_marcelao(A))
        fim = time.time()
        print("tempo do Marcelão: ", fim - ini)
        print("Quantidade de Elementos:", a)
        print(part_marcelao(A))
    else:
        ini = time.time()
        a = len(part_matheusao(A))
        fim = time.time()
        print("tempo do Matheusão: ", fim - ini)
        print("Quantidade de Elementos:", a)


def part_marcelao(a):
    resultado = [[]]
    for i in a:
        resultado += [sub + [i] for sub in resultado]
    return resultado


def part_matheusao(a):
    tam_p = 2 ** len(a)
    partes = []
    for i in range(tam_p):
        sc = []
        for j in range(len(a)):
            if (i & (2 ** j)) > 0:
                sc.append(a[j])
        partes.append(sc)
    return partes


if __name__ == "__main__":
    main()
