import secrets
import string

# Aceasta functionalitate ar putea fi utilizata pentru sugerarea unei parole puternice/sigure
def password_generator():
    password = ''.join(secrets.choice(string.ascii_letters + string.digits + '.!$@') for _ in range(10))
    return password

print("Generare parola sigura: ", password_generator)

# Aceasta functionalitate poate fi utilizata pentru generarea de token-uri pentru autentificare
def URL_generator(length):
    return secrets.token_urlsafe(length)

print("Generare URL: ", URL_generator(32))

# Aceasta functionalitate poate fi folosita pentru generarea de identificatori unici intr-un sistem
def hextoken_generator(length):
    return secrets.token_hex(length)

print("Generare token hexazecimal", hextoken_generator(32))

# Aceasta functionalitate verifica daca 2 secvente sunt identice sau nu, minimizand riscul unui atac de timp
def secure_compare(a, b):
    return secrets.compare_digest(a, b)

print("Compararea sigura a 2 secvente: ")
print("Secventa 1: ")
s1 = input()
print("Secventa 2: ")
s2 = input()

if secure_compare(s1, s2):
    print("Secventele sunt identice.")
else:
    print("Secventele nu sunt identice.")

# Aceasta functionalitate gneereaza o cheie fluida binara care poate fi folosita pentru criptarea unui mesaj de 100 de caractere
def binarykey_generator(length):
    return secrets.token_bytes(length)

print("Generare cheie binara: ", binarykey_generator(100))

# Aceasta functionalitate stocheaza parole care sa ofere un nivel suficien de securitate
# bcrypt ofera functii de hashare sigura si ingreuneaza atacurile de tip rainbow table sau brute force
print("Stocare sigura a parolei: ")
print("Parola: ")

import bcrypt

password = input()
hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
print("Parola criptata: ", hashed_password)