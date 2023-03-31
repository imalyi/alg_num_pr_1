import math

argumenty = [[0, 0], [1, 1], [4, 2], [9, 3], [16, 4], [25, 5], [36, 6], [49, 7], [64, 8], [81, 9]]

współczynniki = [[0 for x in range(10)] for y in range(10)]


def pomnóż(arr1, arr2):
    """
    Funkcja oblicza iloczyn dwóch wektorów reprezentowanych jako listy arr1 i arr2.
    Argumenty:
    arr1 -- wektor pierwszy
    arr2 -- wektor drugi
    Zwraca:
    Wynikowy wektor będący iloczynem wektorów arr1 i arr2.
    """
    wynik = [0 for _ in range(25)]
    for x in range(len(arr1)):
        for y in range(len(arr2)):
            wynik[x + y] += arr1[x] * arr2[y]
    return wynik


def dodaj(arr1, arr2):
    """
    Funkcja oblicza sumę dwóch wektorów reprezentowanych jako listy arr1 i arr2.
    Argumenty:
    arr1 -- wektor pierwszy
    arr2 -- wektor drugi
    Zwraca:
    Wynikowy wektor będący sumą wektorów arr1 i arr2.
    """
    for x in range(len(arr1)):
        arr1[x] += arr2[x]
    return arr1


def wielomian(wiel, n):
    """
    Funkcja oblicza wartość wielomianu o współczynnikach reprezentowanych przez listę wiel w punkcie n.
    Argumenty:
    wiel -- lista zawierająca współczynniki wielomianu
    n -- punkt, w którym ma zostać obliczona wartość wielomianu
    Zwraca:
    Wartość wielomianu o współczynnikach reprezentowanych przez listę wiel w punkcie n.
    """
    suma = 0
    for x in range(len(współczynniki)):
        suma += wiel[x] * math.pow(n, x)
    return suma


def get_bit(num, bit):
    temp = (1 << bit)
    temp = temp & num
    if temp == 0:
        return 0
    return 1


def get_all_subsets(v, sets):
    """
    Funkcja zwraca wszystkie podciągi listy
    """
    subsets_count = 2 ** len(v)
    for i in range(0, subsets_count):
        st = set([])
        for j in range(0, len(v)):
            if get_bit(i, j) == 1:
                tupler = tuple(v[j])
                st.add(tupler)
        sets.append(st)


def policz(subset):
    """
    Funkcja oblicza wielomian interpolacyjny dla zbioru punktów na podstawie metodą Lagrange'a.
    Argumenty:
    od -- indeks początkowego punktu w zbiorze
    do -- indeks końcowego punktu w zbiorze
    Zwraca:
    Wynikowy wielomian interpolacyjny dla punktów od indeksu od do indeksu do.
    """
    subset = list(subset)
    współczynniki = [[0 for _ in range(10)] for _ in range(10)]
    for x in range(len(subset)):
        pierwszy = True
        for y in range(len(subset)):
            if x == y:
                continue
            iloczyn = [-subset[y][0], 1]
            iloraz = subset[x][0] - subset[y][0]
            if pierwszy:
                współczynniki[x][0] = iloczyn[0]
                współczynniki[x][1] = iloczyn[1]
                for z in range(len(współczynniki[x])):
                    współczynniki[x][z] /= iloraz
                pierwszy = False
            else:
                wynik = pomnóż(współczynniki[x], iloczyn)
                for z in range(len(współczynniki[x])):
                    współczynniki[x][z] = wynik[z]
                for z in range(len(współczynniki[x])):
                    współczynniki[x][z] /= iloraz

    wynik = [0 for _ in range(15)]
    for x in range(len(subset)):
        d = subset[x][1]
        wynik = dodaj(wynik, pomnóż(współczynniki[x], [d]))
    return wielomian(wynik, 23)


def main():
    """
    Funkcja oblicza i wyświetla przybliżenia pierwiastka liczby 23 dla każdej
    pary punktów znajdujących się w liście `argumenty`.
    Następnie wyświetla najdokładniejsze przybliżenie oraz węzły, które zostały użyte do jego obliczenia.
    """
    mindiff = -1
    bestsubset = []
    subsets = []
    get_all_subsets(argumenty, subsets)
    print(subsets)
    for x in subsets:
        wyn = policz(x)
        diff = math.sqrt(23) - wyn
        if mindiff < 0 or abs(diff) < abs(mindiff):
            mindiff = abs(diff)
            bestsubset = x
        # print("Przybliżenie ", x, " wynik = ", policz(x))
        print("Przybliżenie {:<87}wynik = {:<10}".format(str(x), str(policz(x))))
    print("\n\n--------")
    print("Najbliżej do pierwiastka z 23 (", math.sqrt(23), ") jest przybliżenie stworzone z węzłów:")
    print(bestsubset)
    print("\nDające wartość ", policz(bestsubset))


if __name__ == '__main__':
    main()
