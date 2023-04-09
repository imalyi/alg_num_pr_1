def import_data():
    data = []
    try:
        with open("./data.txt") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                values = line.split()
                if len(values) != 2:
                    print("Błąd: wiersz nie zawiera dwóch liczb oddzielonych spacją!")
                    exit()
                try:
                    x, y = int(values[0]), int(values[1])
                except ValueError:
                    print("Błąd: nie można przekonwertować wartości na liczby całkowite!")
                    exit()
                data.append([x, y])
    except FileNotFoundError:
        print("Błąd: plik nie istnieje!")
        exit()
    return data
