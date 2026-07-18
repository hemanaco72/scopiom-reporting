"""Chiffre/dechiffre .env pour permettre de commiter une copie de secours
(.env.encrypted) sans exposer les cles API en clair dans le depot git.

La cle de chiffrement vit DELIBEREMENT en dehors du depot, dans le dossier
utilisateur (C:\\Users\\Julien\\.scopiom-vault.key) : jamais commitee, jamais
poussee sur GitHub. Sans cette cle, .env.encrypted est illisible.

Important : ceci protege contre une fuite du depot git (repo rendu public
par erreur, clone non autorise, etc.), PAS contre un acces a l'environnement
cloud des routines (qui n'a de toute facon jamais eu ces cles, cf. CLAUDE.md
S10.4/S10.5 - c'est une limite d'architecture separee, pas resolue par ce
chiffrement).

Usage :
  python scripts/vault.py encrypt   # .env -> .env.encrypted (genere la cle si absente)
  python scripts/vault.py decrypt   # .env.encrypted -> .env (ex. sur une nouvelle machine)
"""

import os
import sys

from cryptography.fernet import Fernet

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ENV_PATH = os.path.join(PROJECT_ROOT, ".env")
ENCRYPTED_PATH = os.path.join(PROJECT_ROOT, ".env.encrypted")
KEY_PATH = os.path.join(os.path.expanduser("~"), ".scopiom-vault.key")


def load_or_create_key() -> bytes:
    if os.path.exists(KEY_PATH):
        with open(KEY_PATH, "rb") as f:
            return f.read().strip()
    key = Fernet.generate_key()
    with open(KEY_PATH, "wb") as f:
        f.write(key)
    print(f"Nouvelle cle de chiffrement generee : {KEY_PATH}")
    print("IMPORTANT : sauvegarde ce fichier ailleurs (hors du depot git). Sans lui, .env.encrypted est definitivement illisible.")
    return key


def encrypt() -> None:
    if not os.path.exists(ENV_PATH):
        print(f"{ENV_PATH} introuvable, rien a chiffrer.", file=sys.stderr)
        sys.exit(1)
    key = load_or_create_key()
    fernet = Fernet(key)
    with open(ENV_PATH, "rb") as f:
        plaintext = f.read()
    with open(ENCRYPTED_PATH, "wb") as f:
        f.write(fernet.encrypt(plaintext))
    print(f"{ENV_PATH} -> {ENCRYPTED_PATH} (chiffre, peut etre commite)")


def decrypt() -> None:
    if not os.path.exists(ENCRYPTED_PATH):
        print(f"{ENCRYPTED_PATH} introuvable.", file=sys.stderr)
        sys.exit(1)
    if not os.path.exists(KEY_PATH):
        print(f"Cle introuvable : {KEY_PATH}. Restaure-la depuis ta sauvegarde avant de dechiffrer.", file=sys.stderr)
        sys.exit(1)
    key = load_or_create_key()
    fernet = Fernet(key)
    with open(ENCRYPTED_PATH, "rb") as f:
        ciphertext = f.read()
    with open(ENV_PATH, "wb") as f:
        f.write(fernet.decrypt(ciphertext))
    print(f"{ENCRYPTED_PATH} -> {ENV_PATH} (dechiffre)")


if __name__ == "__main__":
    if len(sys.argv) != 2 or sys.argv[1] not in ("encrypt", "decrypt"):
        print("Usage: python scripts/vault.py [encrypt|decrypt]", file=sys.stderr)
        sys.exit(1)
    {"encrypt": encrypt, "decrypt": decrypt}[sys.argv[1]]()
