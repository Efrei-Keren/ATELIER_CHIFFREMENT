import os
import base64
from nacl.secret import SecretBox
from nacl.utils import random

# Récupérer la clé depuis l'environnement (32 bytes en base64)
key_b64 = os.getenv("SECRETBOX_KEY")

if not key_b64:
    raise ValueError("SECRETBOX_KEY n'est pas définie dans l'environnement")

key = base64.b64decode(key_b64)

if len(key) != 32:
    raise ValueError("La clé SecretBox doit faire 32 bytes")

box = SecretBox(key)

def encrypt(message: str) -> str:
    nonce = random(24)
    encrypted = box.encrypt(message.encode(), nonce)
    return base64.b64encode(encrypted).decode()

def decrypt(token: str) -> str:
    data = base64.b64decode(token)
    decrypted = box.decrypt(data)
    return decrypted.decode()

if __name__ == "__main__":
    msg = "Atelier 2 - SecretBox PyNaCl"

    print("Message original:", msg)

    encrypted = encrypt(msg)
    print("Chiffré:", encrypted)

    decrypted = decrypt(encrypted)
    print("Déchiffré:", decrypted)
