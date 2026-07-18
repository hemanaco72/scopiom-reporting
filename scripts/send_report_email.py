"""Envoie le dernier rapport ScopIOM (reports/*.xlsx) par email via l'API transactionnelle Brevo.

Usage: python scripts/send_report_email.py [--to jda@mpitech.com] [--file reports/xxx.xlsx]

Necessite BREVO_API_KEY dans un fichier .env a la racine du projet (jamais commite, voir .gitignore).
"""

import argparse
import base64
import glob
import os
import sys

import requests
from dotenv import load_dotenv

BREVO_API_URL = "https://api.brevo.com/v3/smtp/email"
DEFAULT_SENDER = {"name": "ScopIOM Reporting", "email": "webmaster@mpitech.com"}
DEFAULT_RECIPIENT = "jda@mpitech.com"


def latest_report(reports_dir: str) -> str:
    candidates = sorted(
        glob.glob(os.path.join(reports_dir, "rapport-*.xlsx")),
        key=os.path.getmtime,
        reverse=True,
    )
    if not candidates:
        raise FileNotFoundError(f"Aucun rapport .xlsx trouve dans {reports_dir}")
    return candidates[0]


def send_report(file_path: str, to_email: str) -> None:
    api_key = os.environ.get("BREVO_API_KEY")
    if not api_key:
        raise RuntimeError("BREVO_API_KEY manquant : verifie le fichier .env")

    with open(file_path, "rb") as f:
        content_b64 = base64.b64encode(f.read()).decode("ascii")

    filename = os.path.basename(file_path)
    payload = {
        "sender": DEFAULT_SENDER,
        "to": [{"email": to_email}],
        "subject": f"Rapport scopiom.com - {filename}",
        "htmlContent": (
            "<p>Bonjour,</p>"
            f"<p>Veuillez trouver ci-joint le rapport ScopIOM : <strong>{filename}</strong>.</p>"
            "<p>Ce message a ete envoye automatiquement par la routine de reporting scopiom-reporting.</p>"
        ),
        "attachment": [{"content": content_b64, "name": filename}],
    }

    response = requests.post(
        BREVO_API_URL,
        json=payload,
        headers={
            "api-key": api_key,
            "Content-Type": "application/json",
            "Accept": "application/json",
        },
        timeout=30,
    )

    if response.status_code >= 300:
        raise RuntimeError(f"Echec envoi Brevo ({response.status_code}): {response.text}")

    print(f"Envoye avec succes a {to_email} : {filename} (messageId={response.json().get('messageId')})")


if __name__ == "__main__":
    load_dotenv()
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--to", default=DEFAULT_RECIPIENT, help="Destinataire (defaut: jda@mpitech.com)")
    parser.add_argument("--file", default=None, help="Chemin du rapport a envoyer (defaut: le plus recent dans reports/)")
    args = parser.parse_args()

    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    reports_dir = os.path.join(project_root, "reports")

    try:
        file_path = args.file or latest_report(reports_dir)
        send_report(file_path, args.to)
    except Exception as exc:
        print(f"Erreur : {exc}", file=sys.stderr)
        sys.exit(1)
