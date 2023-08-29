import time

def timer(seconds):
    print(f"Timer avviato per {seconds} secondi.")
    time.sleep(seconds)
    print("Timer scaduto!")

if __name__ == "__main__":
    try:
        duration = int(input("Inserisci la durata del timer in secondi: "))
        timer(duration)
    except ValueError:
        print("Inserisci un numero valido per la durata del timer.")

input()