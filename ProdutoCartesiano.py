def main():
    A = [1, 2]
    B = [4, 5]

    print(XCartesiano(A, B))


def XCartesiano(a, b):
    if not a: return b
    if not b: return a

    c = []
    for i in range(len(a)):
        for j in range(len(b)):
            c.append((a[i], b[j]))

    return c


if __name__ == "__main__":
    main()
