import random
import string

def generate_random_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    try:
        password_length = int(input("Inserisci la lunghezza desiderata della password: "))
        if password_length <= 0:
            print("La lunghezza della password deve essere maggiore di 0.")
        else:
            password = generate_random_password(password_length)
            print("Password generata:", password)
    except ValueError:
        print("Inserisci un numero valido per la lunghezza della password.")

if __name__ == "__main__":
    main()

input()             