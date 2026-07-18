"""Test de connexion directe a l'API Semrush (hors MCP) : verifie la cle et le solde
d'unites API. Teste aussi historiquement (18/07/2026) la recuperation des mots-cles
de la campagne Position Tracking "ScopIOM - SEO" (projet 30407302, campagne 5126938) :
CONCLUSION - aucun endpoint public (v3 classique ou v4) ne donne acces a ces donnees
avec cette cle. Confirme via la doc officielle developer.semrush.com/api/v4/ (Projects
API, Local API) qu'aucun endpoint Position Tracking n'y est documente, et les types v3
"tracking_gettargets"/"tracking_position_organic" renvoient "query type not found".
Cf. CLAUDE.md S5.4 : solution retenue = lecture du dashboard via Claude in Chrome.

Usage: python scripts/test_semrush_api.py
Necessite SEMRUSH_API_KEY dans .env (non commite).
"""

import os
import sys

import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.environ.get("SEMRUSH_API_KEY")
if not API_KEY:
    print("SEMRUSH_API_KEY manquant dans .env", file=sys.stderr)
    sys.exit(1)

PROJECT_ID = "30407302"  # "ScopIOM - SEO"
CAMPAIGN_ID = "5126938"  # Position Tracking


def check_balance(label):
    r = requests.get(
        "https://www.semrush.com/users/countapiunits.html",
        params={"key": API_KEY},
        timeout=20,
    )
    print(f"[{label}] Solde unites API restant : {r.text.strip()}")
    return r.text.strip()


def try_call(label, url, params):
    print(f"\n--- {label} ---")
    print(f"GET {url} params={ {k: v for k, v in params.items() if k != 'key'} }")
    r = requests.get(url, params=params, timeout=20)
    print(f"HTTP {r.status_code}")
    body = r.text[:800]
    print(f"Reponse (800 premiers caracteres) : {body}")
    return r


if __name__ == "__main__":
    balance_before = check_balance("AVANT")

    # Liste des projets (Project Management API) - fonctionne, cout faible.
    try_call(
        "Liste des projets",
        "https://api.semrush.com/management/v1/projects",
        {"key": API_KEY},
    )

    # NOTE (18/07/2026) : aucun endpoint fonctionnel trouve pour recuperer les
    # mots-cles/positions de la campagne Position Tracking (projet PROJECT_ID,
    # campagne CAMPAIGN_ID). Teste et echoue : type=tracking_gettargets et
    # type=tracking_position_organic sur l'API classique (HTTP 400 "query type
    # not found"). Aucun endpoint equivalent documente dans l'API v4 (Projects
    # API, Local API). Solution retenue : lecture du dashboard via Claude in
    # Chrome, cf. CLAUDE.md S5.4.

    balance_after = check_balance("APRES")

    print(f"\nConsommation estimee : {balance_before} -> {balance_after}")
