def main():
    print("Benvenuto!")
    nome = input("Qual è il tuo nome? ")
    anno_di_nascita = int(input("In che anno sei nato/a? "))
    
    anno_corrente = 2023
    
    eta = anno_corrente - anno_di_nascita
    print(f"Ciao, {nome}! Hai {eta} anni.")

if __name__ == "__main__":
    main()

input()             