import math

argumenty = [0,1,4,9,16,25,36,49,64,81]
wartości = [0,1,2,3,4,5,6,7,8,9]

współczynniki = [[0 for x in range(10)] for y in range(10)]

def pomnóż(arr1,arr2):
    """
    Funkcja oblicza iloczyn dwóch wektorów reprezentowanych jako listy arr1 i arr2.

    Argumenty:
    arr1 -- wektor pierwszy
    arr2 -- wektor drugi

    Zwraca:
    Wynikowy wektor będący iloczynem wektorów arr1 i arr2.
    """
    wynik = [0 for x in range(25)]
    for x in range(len(arr1)):
        for y in range(len(arr2)):
            wynik[x+y]+=arr1[x]*arr2[y]
    return wynik

def dodaj(arr1,arr2):
     """
    Funkcja oblicza sumę dwóch wektorów reprezentowanych jako listy arr1 i arr2.

    Argumenty:
    arr1 -- wektor pierwszy
    arr2 -- wektor drugi

    Zwraca:
    Wynikowy wektor będący sumą wektorów arr1 i arr2.
    """
    for x in range(len(arr1)):
        arr1[x]+=arr2[x]
    return arr1

def wielomian(wiel,n):
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
        suma+=wiel[x]*math.pow(n,x)
    return suma

def policz(od,do):
    """
    Funkcja oblicza wielomian interpolacyjny dla zbioru punktów na podstawie metodą Lagrange'a.

    Argumenty:
    od -- indeks początkowego punktu w zbiorze
    do -- indeks końcowego punktu w zbiorze

    Zwraca:
    Wynikowy wielomian interpolacyjny dla punktów od indeksu od do indeksu do.
    """
    współczynniki = [[0 for x in range(10)] for y in range(10)]
    for x in range(od,do+1):
        pierwszy = True
        for y in range(od,do+1):
            if x==y:
                continue
            iloczyn = []
            iloczyn.append(-argumenty[y])
            iloczyn.append(1)
            iloraz = argumenty[x]-argumenty[y]
            if pierwszy:
                współczynniki[x][0]=iloczyn[0]
                współczynniki[x][1] = iloczyn[1]
                for z in range(len(współczynniki[x])):
                    współczynniki[x][z]/=iloraz
                pierwszy = False
            else:
                wynik = pomnóż(współczynniki[x],iloczyn)
                for z in range(len(współczynniki[x])):
                    współczynniki[x][z] = wynik[z]
                for z in range(len(współczynniki[x])):
                    współczynniki[x][z]/=iloraz

    wynik = [0 for x in range(15)]
    for x in range(len(współczynniki)):
        wynik=dodaj(wynik,pomnóż(współczynniki[x],[wartości[x]]))
    return(wielomian(wynik,23))


def main():
    """
    Funkcja oblicza i wyświetla przybliżenia pierwiastka liczby 23 dla każdej
    pary punktów znajdujących się w liście `argumenty`.
    Następnie wyświetla najdokładniejsze przybliżenie oraz węzły, które zostały użyte do jego obliczenia.
    """
    mindiff = -1
    najlepszeod = 0
    najlepszedo = 0
    for x in range(len(argumenty)):
        for y in range(x+1,len(argumenty)):
            wyn = policz(x,y)
            diff = math.sqrt(23)-wyn
            if mindiff<0 or abs(diff)<abs(mindiff):
                mindiff=abs(diff)
                najlepszeod=x
                najlepszedo=y
            print("Przybliżenie od ",argumenty[x]," do ",argumenty[y]," wynik = ",policz(x,y))


print("\n\n--------")
print("Najbliżej do pierwiastka z 23 (",math.sqrt(23),") jest przybliżenie stworzone z węzłów:")
print('{:6s}'.format("x: "),end="")
for x in range(najlepszeod,najlepszedo):
    print('{:2d}'.format(argumenty[x]),end=" ")
print("")
print('{:6s}'.format("f(x): "),end="")
for x in range(najlepszeod,najlepszedo):
    print('{:2d}'.format(wartości[x]),end=" ")
print("\nDające wartość ",policz(najlepszeod,najlepszedo))
