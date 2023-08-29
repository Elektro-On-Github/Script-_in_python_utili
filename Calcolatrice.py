def addizione(x, y):
    return x + y

def sottrazione(x, y):
    return x - y

def moltiplicazione(x, y):
    return x * y

def divisione(x, y):
    if y != 0:
        return x / y
    else:
        return "Errore: divisione per zero"

def main():
    print("Seleziona l'operazione:")
    print("1. Addizione")
    print("2. Sottrazione")
    print("3. Moltiplicazione")
    print("4. Divisione")

    scelta = input("Inserisci la scelta (1/2/3/4): ")

    num1 = float(input("Inserisci il primo numero: "))
    num2 = float(input("Inserisci il secondo numero: "))

    if scelta == '1':
        print("Risultato:", addizione(num1, num2))
    elif scelta == '2':
        print("Risultato:", sottrazione(num1, num2))
    elif scelta == '3':
        print("Risultato:", moltiplicazione(num1, num2))
    elif scelta == '4':
        print("Risultato:", divisione(num1, num2))
    else:
        print("Scelta non valida")

if __name__ == "__main__":
    main()

input()