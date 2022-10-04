def main():

    N = input()
    print(AlgarismosSignificativos(N))

def AlgarismosSignificativos(x):
    count = 0
    x = x.replace(',', '')
    x = x.replace(' ', '')


    for i in range(len(x)):
        if x[i] != '0':
            lim = i
            break

    for i in range(lim, len(x)):
        count += 1

    return count

if __name__ == '__main__':
    main()
