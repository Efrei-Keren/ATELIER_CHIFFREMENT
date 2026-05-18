import os
from cryptography.fernet import Fernet

# Récupérer la clé depuis GitHub Secret (env variable)
key = os.getenv("FERNET_KEY")

if not key:
    raise ValueError("FERNET_KEY n'est pas définie dans l'environnement")

fernet = Fernet(key)

def encrypt_text(message: str) -> str:
    return fernet.encrypt(message.encode()).decode()

def decrypt_text(token: str) -> str:
    return fernet.decrypt(token.encode()).decode()

if __name__ == "__main__":
    msg = "Atelier 1 - secret GitHub"

    print("Message original:", msg)

    encrypted = encrypt_text(msg)
    print("Chiffré:", encrypted)

    decrypted = decrypt_text(encrypted)
    print("Déchiffré:", decrypted)
