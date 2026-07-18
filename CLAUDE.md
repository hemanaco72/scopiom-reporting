# Contexte projet — ScopIOM Reporting & Veille SEO/IA

Ce fichier est la mémoire permanente du projet `scopiom-reporting`. Chaque session Claude Code lancée dans ce dossier le lit automatiquement. Il doit rester à jour : si une information change (nouveau concurrent, nouveau mot-clé, nouvelle règle éditoriale), modifiez ce fichier en conséquence plutôt que de le laisser devenir obsolète.

---

## 1. Identité produit

- **Éditeur** : MPI Tech, éditeur logiciel français indépendant, fondé en **1981**. Siège : 40 avenue du Général Malleret Joinville, 94400 Vitry-sur-Seine.
- **Toujours écrire "MPI Tech"**. Ne jamais écrire "Data Syscom" (ancien nom, présent par erreur dans d'anciens documents internes — à corriger partout où on le croise).
- **Produit** : ScopIOM™, plateforme d'Output Management et d'orchestration documentaire (version actuelle : **v6.0**), 100 % on-premise, souveraine.
- **Cible** : DSI, architectes d'entreprise, décideurs grands comptes — banque, assurance, mutuelle, industrie multisite, centres éditiques, administration publique.
- **ScopTracking™** est un produit à part entière (UI et base MongoDB indépendantes), ce n'est **pas** un module de ScopIOM.
- **iSeries/AS400** est une plateforme serveur, **pas un ERP** : elle génère des flux d'impression via des spouleurs IBM natifs (IPDS, AFP). À traiter comme un environnement d'émission distinct dans tout contenu technique.
- Terminologie imposée : toujours **"tables d'exploitation"**, jamais "Operating Table".

---

## 2. Environnement technique du site

- **Stack** : WordPress, Divi 5, Divi Pixel, Rank Math PRO, WPML, Code Snippets, Complianz, Hummingbird, WP Defender Pro, Brevo (SMTP via WP Mail SMTP).
- **Hébergement** : Kinsta, avec Cloudflare devant (bloque l'accès direct par curl — passer par `web_fetch` ou Claude in Chrome pour toute inspection).
- **Staging** : `stg-scopiom-staging.kinsta.cloud` (accessible publiquement, doit rester en `noindex`).
- **Dette technique connue à date** :
  - CLS desktop très au-dessus du seuil "poor" Google (cause probable : wrapper hero + police d'icônes Divi sans `font-display: swap`).
  - LCP mobile en zone "poor" sur PageSpeed Insights.
  - Accessibilité PageSpeed : 86/100 (mobile et desktop).
  - Conformité RGAA estimée à ~92 % ; contrastes à corriger sur `.feat-num-label`, `.dipi-at-tab-subtitle`, `.gd-label`.
  - Schema : blocs FAQPage (Divi Pixel) et schema custom Rank Math en conflit (nesting corrompu, à nettoyer) ; SoftwareApplication limité à la homepage.
  - 26-27 URLs indexées à date.

---

## 3. Objectif SEO n°1

**Dépasser Sefas Innovation et SEAL Systems sur "output management system"** (marché français). C'est le mot-clé prioritaire absolu.

⚠️ **Mise à jour du 18/07/2026 (voir §7 pour la source)** : la position 1 a changé depuis la rédaction initiale de cette section. **Sefas Innovation (sefasinnovation.fr) occupe désormais la position 1**, SEAL Systems est passé en position 2. mpitech.com (le site corporate MPI Tech, pas scopiom.com) apparaît en position 7 — scopiom.com, pourtant le site produit pivot de toute la stratégie, n'a toujours aucun mot-clé organique dans la base Semrush FR. L'objectif ci-dessous et le raisonnement par différenciation restent valables et s'appliquent aussi face à Sefas (voir profil concurrent §4.1, notamment le rachat par Messagepoint qui renforce l'angle souveraineté).

Constat qui rend cet objectif atteignable : le territoire sémantique français est largement libre. Aucun mot-clé cible prioritaire ne dépasse KD 27, et le concurrent en position 1 tient sa place avec un seul article de blog relativement faible.

Angles de différenciation à exploiter systématiquement dans le contenu :
- ERP-agnostic (SEAL est lié à SAP/PLOSSYS/BC-XOM) vs. spécifique SAP.
- Ordonnancement au niveau métier, absent chez SEAL.
- Aucun concurrent français ne capte de Featured Snippet sur ce territoire — ScopIOM peut le faire.
- Multisite : absent chez SEAL.
- On-premise souverain vs. concurrents plus orientés cloud.
- Conformité WCAG/RGAA : non traitée par SEAL.
- Ton institutionnel froid chez les concurrents allemands vs. langage terrain DSI chez ScopIOM.

**Contenu prioritaire en attente de rédaction** : article "Migration SAP S/4HANA et output management" (KD 8).

---

## 4. Paysage concurrentiel

### 4.1. Concurrents directs (Output Management / CCM)

| Éditeur | Produit | Origine | Points clés |
|---|---|---|---|
| **SEAL Systems** | Plossys / BC-XOM | Allemagne | Concurrent n°1 à battre en France. Fort lien SAP. Blog actif depuis avril 2026, rythme de publication soutenu — à surveiller régulièrement (voir §7). |
| **Compart** | DocBridge® (DocBridge Pilot, DocBridge Mill...) | Allemagne (Böblingen) | Page produit en anglais uniquement, pas de présence FR dédiée. Historiquement très fort sur la conversion de flux d'impression (AFP, PCL, PostScript) et l'archivage. |
| **LRS** (Levi, Ray & Shoup) | VPSX (Output Management Suite) | USA (Springfield, Illinois) | Référence historique du marché, très forte intégration SAP/IBM z/OS/IBM i, absent des SERP françaises. Positionnement très mainframe/grands comptes internationaux. |
| **Sefas** | Harmonie Communication Suite (composition, ECP, orchestration omnicanale) | France (Ivry-sur-Seine), fondé en 1991 | ⚠️ **Rachat récent** : ex-filiale de Docaposte (Groupe La Poste), Sefas a été **acquis par Messagepoint (Toronto, Canada) le 5 mars 2026**. L'éditeur n'est donc plus sous capital français — argument de différenciation direct pour le narratif souveraineté de ScopIOM. Positionnement CCM/ECP plutôt que pur Output Management technique. |
| **Formpipe (Lasernet)** | Lasernet | Suède | Très spécialisé sur l'intégration ERP (Microsoft Dynamics 365/AX, IFS Cloud, Temenos pour le secteur bancaire). Angle « no-code » pour la génération de documents depuis l'ERP. Peu présent sur le terrain pur spooling/impression haute disponibilité. |
| **Objectif Lune** | OL Connect | Devenu **Upland Objectif Lune**, société mère Upland Software (Austin, Texas, USA) | Éditeur d'origine québécoise, aujourd'hui capital américain. Positionnement middleware de composition documentaire pour moderniser les sorties ERP/mainframe sans les remplacer. |
| **Papyrus** (ISIS Papyrus) | WebControl | Autriche | Alternative européenne complète EOM + CCM. |
| **OpenText** | Output Management (module) | Canada | Domaine trop large pour un suivi de share-of-voice précis — ajouter l'URL produit spécifique (VPOM) si disponible. |
| **Quadient** | GMC Inspire | France/USA | Principalement une plateforme CCM ; ne remplace pas nécessairement une solution EOM complète. |
| **Ricoh** | ProcessDirector | Japon | Très orienté centres éditiques industriels, moins orienté réseau d'agences. |
| **Pitney Bowes** | EngageOne | USA | — |
| **Crawford Technologies** | PRO | Canada | — |
| **HP (Dazel / HP Output Server)** | HP Output Server (HPOS) | USA — ex-Dazel Corp (Austin, Texas), racheté par HP en 2001 | Produit **legacy** : plus activement commercialisé par HP, mais encore en support et utilisé par de grands comptes (témoignages 2024-2025 de migrations Solaris→SUSE toujours en cours). Angle de contenu fort et peu exploité : LRS et Plus Technologies ciblent déjà activement les clients "encore sous Dazel/HPOS" pour des migrations — ScopIOM peut faire de même. "dazel" seul obtient 40 recherches/mois en France, KD 0 (vérifié Semrush 18/07/2026).

### 4.1bis. Mouvement de consolidation du marché — angle éditorial à exploiter

Plusieurs acteurs historiquement positionnés comme "européens" ou "indépendants" sont passés sous capital étranger récemment : Sefas (français, ex-Docaposte) est passé sous pavillon canadien via Messagepoint en mars 2026 ; Objectif Lune (québécois à l'origine) est intégré depuis plusieurs années au groupe américain Upland Software. **ScopIOM reste un éditeur français indépendant depuis 1981** : c'est un argument factuel et vérifiable à mobiliser dans tout contenu ciblant les critères de souveraineté (administration, banque, secteurs régulés), sans dénigrer les concurrents — se contenter d'énoncer les faits d'actionnariat, vérifiables publiquement.

### 4.2. Tableau comparatif fonctionnel détaillé

*Ce tableau reprend l'analyse comparative interne existante (6 éditeurs). Sefas, Formpipe/Lasernet et Objectif Lune ont été ajoutés au panorama concurrentiel du §4.1 mais n'ont pas encore été passés au crible des mêmes critères ligne par ligne — à faire si un contenu les compare frontalement à ScopIOM.*

Légende : ✅ capacité documentée · ◐ partielle/à confirmer · ⚠️ dépend du module/déploiement · ❌ non identifiée

| Critère | ScopIOM | LRS VPSX | Papyrus | Ricoh PD | Quadient | OpenText |
|---|:---:|:---:|:---:|:---:|:---:|:---:|
| On-premise | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Sans dépendance cloud | ✅ | ✅ | ✅ | ✅ | ⚠️ | ⚠️ |
| Spooling distribué multisite | ◐ | ✅ | ✅ | ◐ | ❌ | ❌ |
| Haute disponibilité | ◐ | ✅ | ✅ | ✅ | ◐ | ◐ |
| SAP | ◐ | ✅ | ✅ | ✅ | ✅ | ✅ |
| IBM i / AS400 | ✅ | ✅ | ✅ | ◐ | ◐ | ◐ |
| AFP / IPDS | ✅ | ✅ | ✅ | ✅ | ◐ | ◐ |
| Réseau de centaines de sites | ✅ | ✅ | ✅ | ◐ | ❌ | ❌ |
| Éditeur français | ✅ | ❌ | ❌ | ❌ | ✅ | ❌ |
| Niveau de souveraineté | ⭐⭐⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐ |

*(API REST/Web Services et LDAP/AD sont marqués "à valider" côté ScopIOM dans ce comparatif — à vérifier avant toute publication qui s'appuierait dessus ; les réponses RFI internes confirment cependant une API REST existante et documentée, voir §9.)*

**Recommandation par contexte client** (issue de l'analyse comparative interne) :
- Administration / banque / secteur public → ScopIOM en tête, puis Papyrus, puis LRS.
- Environnements SAP/IBM lourds, grands groupes internationaux → LRS en tête, puis Papyrus, puis ScopIOM.
- Centre éditique industriel pur → Ricoh ProcessDirector en tête.

### 4.3. Écosystème partenaires / intégrations

- **ERP** : SAP (natif BC-XOM/S4HANA), Oracle, Sage.
- **IBM** : acteur central — MPI Tech expert AFP/IPDS, iSeries/AS400.
- **CCM** : Quadient Inspire, OpenText Exstream, Smart Communications.
- **Impression** : PaperCut, Pharos, Canon Uniflow, Printix.
- **Spooling** : ThinPrint, PrinterLogic.
- **Institutionnel** : ANSSI, DINUM, AFNOR, GS1.

### 4.4. Snapshot SERP le plus récent (analyse Semrush, avril 2026 — **obsolète, voir mise à jour ci-dessous**)

| Concurrent | Position sur "output management system" | Trafic mensuel estimé |
|---|---|---|
| SEAL Systems | 1 | 218 visites/mois |
| LRS | 5 | 21 visites/mois |
| Compart | 7 | 16 visites/mois |
| ScopIOM | absent | objectif : top 3 |

**Mise à jour au 18/07/2026 (requête SERP Semrush live, confirmée aussi au §7)** : **Sefas Innovation (sefasinnovation.fr) en position 1**, **SEAL Systems en position 2**, **mpitech.com en position 7** (site corporate MPI Tech, pas scopiom.com), **scopiom.com toujours absent** du top 20 et sans aucun mot-clé organique en base Semrush FR. La table ci-dessus (avril 2026) est conservée pour l'historique mais ne doit plus être citée comme l'état actuel.

Cette donnée date d'avril 2026 : à rafraîchir via le MCP SEMrush (`organic_research` / `position_tracking`) dans le rapport hebdomadaire plutôt que de se fier à ce chiffre figé.

---

## 5. Mots-clés & stratégie de contenu

### 5.1. Mots-clés cibles prioritaires (analyse initiale, avril 2026)

| Mot-clé | KD | Volume/mois | Signal |
|---|---|---|---|
| output management system | 18 | 880 | SEAL Systems pos. 1 à battre |
| comment centraliser gestion impressions multisites | 9 | — | Featured Snippet libre, priorité absolue |
| gestion des impressions | 19 | — | Featured Snippet disponible |
| failover imprimante automatique | 14 | — | Featured Snippet libre |
| spouler les documents | 27 | — | Featured Snippet libre, Compart en position 48 |
| logiciel éditique banque assurance | 11 | — | Aucun concurrent positionné |
| centre éditique logiciel ordonnancement | 12 | — | People Also Ask disponible |
| alternative OpenText output manager | 17 | — | Intent commercial fort, décision d'achat |
| gestion flux documentaires entreprise | 12 | — | People Also Ask disponible |
| supervision impressions réseau | 10 | — | Featured Snippet disponible |

### 5.2. Articles blog prioritaires en attente

**Mise à jour du 18/07/2026 (rapport mensuel juin 2026)** : en croisant les pages vues GA4 de juin-juillet 2026, deux articles listés ci-dessous comme "en attente" apparaissent en réalité déjà **publiés** sur scopiom.com. Cette table était obsolète sur ce point — corrigée ci-dessous. La vérification directe du contenu (angle éditorial, respect des règles de rédaction §8, distinction des 3 niveaux de failover §9) n'a pas pu être faite par fetch direct (Cloudflare bloque l'accès, HTTP 503) : à confirmer manuellement à l'occasion d'une session avec accès navigateur.

| Article | KD | Statut | Note |
|---|---|---|---|
| Migration SAP S/4HANA et output management | 8 | **PUBLIÉ** (constaté 18/07/2026) | URL `/migration-sap-s-4hana-ne-negligez-pas-loutput-management-de-vos-flux-dimpression/`, 45 pages vues GA4 sur juin-juillet 2026. Encore 0 impression Search Console (page récente / indexation en cours). SEAL Systems avait publié un témoignage client sur ce thème le 13/07/2026 (voir §7) — à comparer une fois le contenu ScopIOM vérifié. |
| Failover imprimante / haute disponibilité | 14 | **PUBLIÉ** (constaté 18/07/2026) | URL `/failover-et-haute-disponibilite/`, 38 pages vues GA4 sur juin-juillet 2026. À vérifier que la distinction des 3 niveaux de failover (§9) y est bien respectée. |
| Output Management : définition, fonctionnement, cas d'usage DSI | 18 | **Statut incertain** | URL `/blog/output-management-definition/` détectée mais seulement 1 page vue sur juin-juillet 2026 : probablement une ébauche ou une ancienne URL, pas un article achevé et promu. 880/mois, vise à dépasser SEAL Systems, qui a publié un article généraliste proche le 15/06/2026 — à vérifier avant de considérer cette priorité comme traitée. |
| Print vs. Output management | 12 | En attente | Aucune URL correspondante détectée dans GA4. SEAL présent mais contenu faible. |
| Comment centraliser la gestion des impressions multisites | 9 | En attente | Aucune URL correspondante détectée dans GA4. Featured Snippet libre. |
| Spouler les documents | 27 | En attente | Aucune URL correspondante détectée dans GA4. Featured Snippet libre. |

### 5.3. Mapping H1 par page parente

| Page | H1 cible |
|---|---|
| Homepage | Vos flux documentaires sous contrôle, de l'entrée à la sortie |
| Solution | ScopIOM — logiciel d'Output Management et d'ordonnancement de flux éditiques |
| Fonctionnalités | Toutes les fonctionnalités ScopIOM pour gérer vos flux d'impression et vos documents |
| Cas d'usage | Comment centraliser la gestion de vos impressions et flux documentaires |
| Ressources | Output Management — définitions, guides et FAQ pour les DSI |

### 5.4. Campagne de suivi Position Tracking — statut réel (corrigé le 18 juillet 2026)

⚠️ **La note qui circulait ("campagne vide, 0 mot-clé", encore présente au §7 avant cette correction) était erronée.** Vérification directe le 18/07/2026 : la campagne existe et tourne depuis le **13 juillet 2026**. Projet **"ScopIOM - SEO"** (id `30407302`), campagne Position Tracking id `5126938`, **41 mots-clés** tagués par cluster. Données réelles constatées le 18/07/2026 : visibilité 0,64 %, position moyenne 97,63, mouvements Top 3/Top 10 déjà enregistrés. Dashboard : `https://fr.semrush.com/tracking/landscape/30407302_5126938.html`.

**Limite d'accès identifiée** : le compte `webmaster@mpitech.com` est sur l'offre **Semrush One Starter** (199 $/mois). Cette offre inclut l'accès MCP pour les outils de base (recherche de mots-clés, liste de projets), mais **pas** l'accès complet aux données de campagne Position Tracking via API, réservé à l'offre **Advanced** (549 $/mois, ex-"Business"). Conséquence : `tracking_position_organic`/`tracking_overview_organic`/`campagns` renvoient "Access denied" au MCP, alors que les appels basiques fonctionnent. Ce n'est pas un problème de permissions de compte, ne pas rechercher de ce côté.

**Test API direct confirmant la limite (18/07/2026)** : `scripts/test_semrush_api.py` teste la connexion en dehors du MCP, avec une clé API dédiée stockée dans `.env` (jamais commitée). Résultats :
- Connexion et clé valides, coût négligeable (~100 unités consommées sur 41 410 disponibles pour tout le test).
- `management/v1/projects` fonctionne et confirme les deux projets (`ScopIOM - SEO` id 30407302, `ScopIOM - IA` id 30404738).
- Aucun endpoint, ni sur l'API classique (`tracking_gettargets`, `tracking_position_organic` → HTTP 400 "query type not found") ni sur l'API v4 documentée (`developer.semrush.com/api/v4/` — Projects API et Local API ne couvrent pas le Position Tracking), ne permet de récupérer les mots-clés/positions de la campagne avec cette clé.
- **Conclusion** : ce n'est pas un problème de nom d'endpoint mal deviné, la fonctionnalité n'est simplement pas exposée publiquement à ce niveau de plan. La solution retenue (lecture du dashboard via Claude in Chrome, décrite plus bas) reste la bonne approche tant que le plan Semrush n'est pas upgradé vers Advanced.

**Solution retenue (sans upgrade)** : ne pas dépendre du MCP SEMrush pour les données de cette campagne. Faire lire le dashboard par **Claude in Chrome** (navigation + lecture d'écran) plutôt que par appel API — voir rappel d'action manuelle au §10.1.

**Architecture du pipeline (décidée le 18/07/2026)** : **Claude in Chrome ne fonctionne que dans une session interactive locale connectée au Chrome de l'utilisateur — les routines cloud (§10.5) n'ont aucun accès navigateur** (`allowed_tools` limité à Bash/Read/Write/Edit/Glob/Grep). Il est donc impossible que la lecture du dashboard Position Tracking se fasse automatiquement le lundi à 8h. Solution retenue : un **snapshot local périodique**.
- Fichier : `data/position-tracking-latest.json`, contient la date du snapshot, les métriques globales (visibilité, position moyenne, Top 3/Top 10), et le détail des mots-clés ayant une position mesurable (la grande majorité des 64 mots-clés suivis n'a aucune position dans le top 100 à ce jour — normal vu le lancement récent de la campagne, mais à documenter, pas à cacher).
- **Processus de rafraîchissement** : à faire manuellement en session interactive (comme celle-ci), idéalement chaque lundi matin avant 8h — naviguer vers `https://www.semrush.com/tracking/overview/{project_id}_{campaign_id}.html`, lire le tableau via Claude in Chrome, régénérer le fichier JSON, committer et pousser.
- **Les routines cloud lisent ce fichier tel quel** (`data/position-tracking-latest.json`) pour la section Position Tracking de leur rapport, et **doivent signaler explicitement l'âge du snapshot** (`snapshot_date`) dans le rapport — ne jamais présenter une donnée vieille de plusieurs semaines comme fraîche. Si le fichier n'existe pas ou est trop ancien (> 10 jours pour le rapport hebdo), le signaler comme donnée manquante plutôt que d'improviser.

**Liste réelle extraite le 18 juillet 2026** (26 mots-clés sur 41 confirmés — le tableau Semrush charge les lignes par lot au scroll, cet export n'en capture qu'une partie ; les 15 restants sont à récupérer via le bouton "Copy all" de la fenêtre Keywords) :

| Cluster (tag Semrush réel) | Mots-clés |
|---|---|
| `pilier générique` | logiciel d'ordonnancement éditique · ordonnancement éditique · solution output management · output management · logiciel output management · éditique définition |
| `concurrentiel alternative` | alternative opentext output management · logiciel output management français · alternative seal systems · alternative quadient gmc inspire |
| `fonctionnalités` | gestion des tables d'exploitation · routage dynamique impression multisite · gestion des files d'attente d'impression · reprise à la page impression · supervision impressions réseau · spooling documents impression |
| `conformité souveraineté` | logiciel souverain output management · hébergement souverain éditique · solution on-premise gestion documentaire |
| `intégrations techniques` | output management sap bc-xom · afp ipds impression mainframe · output management iseries as400 · migration sap s4hana impression · output management sap s/4hana |
| `secteurs` | gestion impressions multisite industrie · centre éditique bancaire |

⚠️ **À vérifier avant tout ajout** : ni "output management system" (720 recherches/mois, mot-clé prioritaire absolu du §3) ni "sefas" ne semblent présents dans ces 26 — ils font peut-être partie des 15 non extraits. Vérifier dans Semrush avant de dupliquer.

Une deuxième campagne est prévue avec ChatGPT comme moteur de recherche, pour comparer visibilité SEO classique et visibilité IA (voir §6).

### 5.5. Mots-clés supplémentaires proposés (18 juillet 2026, à ajouter par Julien)

Le cluster `concurrentiel alternative` ne couvrait que 4 mots-clés (SEAL, OpenText, Quadient — ni Compart, ni LRS, ni Sefas, pourtant tous des concurrents directs, et Sefas vient de passer en position 1 sur le mot-clé prioritaire). Liste ci-dessous à coller dans Semrush (fenêtre Keywords > Tagged Keywords, format `mot-clé, tag`) :

```
output management system, pilier générique
gestion des impressions, pilier générique
gestion documentaire entreprise, pilier générique
éditique, pilier générique
workflow documentaire, pilier générique
solution d'impression, pilier générique
centre éditique, pilier générique
spouler les documents, fonctionnalités
compart docbridge, concurrentiel alternative
alternative compart docbridge, concurrentiel alternative
lrs vpsx, concurrentiel alternative
alternative lrs output management, concurrentiel alternative
sefas harmonie, concurrentiel alternative
sefas innovation avis, concurrentiel alternative
alternative sefas messagepoint, concurrentiel alternative
alternative formpipe lasernet, concurrentiel alternative
alternative objectif lune, concurrentiel alternative
comparatif scopiom seal systems, concurrentiel alternative
seal systems avis, concurrentiel alternative
logiciel éditique assurance, secteurs
output management administration publique, secteurs
gestion impressions mutuelle, secteurs
solution souveraine impression entreprise, conformité souveraineté
éditeur français output management, conformité souveraineté
intégration api rest output management, intégrations techniques
dazel, concurrentiel alternative
remplacer dazel, concurrentiel alternative
migration hp output server, concurrentiel alternative
alternative hp output server, concurrentiel alternative
```

*(Ajout du 18/07/2026, deuxième passe : Dazel/HP Output Server (HPOS), produit legacy racheté par HP en 2001, identifié comme angle de migration peu exploité — voir profil concurrent §4.1. Seul "dazel" a du volume mesuré (40/mois, KD 0) ; les trois variantes migration/alternative n'ont aucun volume mesuré en base Semrush FR mais restent pertinentes pour occuper ce territoire avant que LRS ou Plus Technologies ne le fassent en France.)*

*(Ajout du 18/07/2026 par rapport à la liste initialement proposée : "sefas innovation avis", vu que ce concurrent est maintenant en position 1 sur le mot-clé prioritaire — pas seulement "sefas harmonie" qui ne couvrait que le nom produit.)*

Une fois ajoutés : 41 → 69 mots-clés, très en dessous de la limite de 500 de l'offre Starter. Répartition visée par cluster après ajout : `pilier générique` 13, `concurrentiel alternative` 19, `fonctionnalités` 7, `conformité souveraineté` 5, `intégrations techniques` 6, `secteurs` 5.

---

## 6. Référencement IA (GEO / AEO)

ScopIOM est aujourd'hui le seul éditeur français à produire des ressources francophones sérieuses sur l'Output Management : c'est un avantage compétitif durable à exploiter, pas seulement pour le SEO classique mais pour la visibilité dans les réponses des LLM.

**Pourquoi c'est prioritaire** : quand un DSI interroge ChatGPT, Perplexity ou Gemini sur l'éditique ou l'Output Management, le LLM cite les sources qu'il a indexées et jugées faisant autorité. Aucun concurrent français ne produit ce contenu à ce jour ; Compart et SEAL Systems (tous deux allemands) ont des sites FR faibles ou inexistants.

**Format qui compte pour les LLM comme pour Google** : les définitions du glossaire doivent tenir en 50 mots en début d'entrée — c'est le format que Google extrait pour les Featured Snippets, et c'est aussi celui que les LLM privilégient pour construire leurs réponses. Vérifier systématiquement le nombre de mots avant publication.

**Roadmap GEO/AEO** :
- Campagne SEMrush Position Tracking n°2 avec ChatGPT comme moteur.
- Suivi des mentions de marque dans les réponses IA (ChatGPT, Perplexity, Gemini, Claude).
- Skill dédiée disponible : `searchfit-seo:ai-visibility` pour l'analyse approfondie quand nécessaire.

---

## 7. Veille concurrentielle continue

**Instruction permanente** : le blog de SEAL Systems (`https://www.sealsystems.fr/blog/category/seal-systems-fr/`) est actif et publie à un rythme soutenu depuis avril 2026. Il doit être vérifié régulièrement (idéalement à chaque exécution du rapport hebdomadaire, ou via une routine dédiée) pour détecter tout nouvel article. Quand un nouvel article apparaît :
1. L'analyser (angle, mots-clés visés, éventuel Featured Snippet capté).
2. Noter s'il comble une des lacunes listées au §3 (ERP-agnostic, multisite, ordonnancement métier, RGAA...).
3. Signaler dans le rapport hebdomadaire toute évolution qui change le rapport de force sur "output management system" ou les mots-clés du cluster concurrentiel.

**Dernière vérification : 18/07/2026 (rapport mensuel juin 2026).** Aucun nouvel article depuis le 13/07/2026. Articles constatés sur le blog SEAL Systems, du plus récent au plus ancien (liste étendue jusqu'à mi-avril 2026 à l'occasion de cette vérification) :

| Date | Titre | Angle |
|---|---|---|
| 13/07/2026 | Impressions SAP : le REX d'un groupe de luxe dans l'USF Mag n°70 | Témoignage client, modernisation des impressions SAP lors d'une migration S/4HANA — **chevauche directement l'article prioritaire ScopIOM en attente (§5.2)** |
| 29/06/2026 | Impression SAP sur sites distants sans VPN ? | Impression SAP sur sites distants sans VPN, avec REX |
| 15/06/2026 | Output Management SAP : pourquoi un système d'Output Management fait toute la différence | Cycle de vie documentaire depuis SAP jusqu'à la diffusion — proche de l'article générique ScopIOM en attente (§5.2) |
| 08/06/2026 | USF 2026 à Strasbourg : SEAL Systems présente ses solutions d'Output Management pour SAP | Annonce événementielle, Convention USF (14-15 octobre 2026) |
| 01/06/2026 | Livret : Supply Chain SAP : Pourquoi la gestion des impressions est critique ? | Lead magnet (livret téléchargeable) sur la Supply Chain SAP |
| 26/05/2026 | Gestion des impressions et diffusions SAP : Où en êtes-vous ? | Bilan/questionnement sur la maturité des dispositifs d'impression SAP |
| 18/05/2026 | Qu'est-ce que SAP DMS ? Le module GED SAP expliqué de A à Z | GED SAP, hors périmètre Output Management pur |
| 11/05/2026 | Comment générer des Dossiers de Fabrication SAP ? Le guide complet | Cas d'usage industriel SAP |
| 04/05/2026 | Adobe Forms (ADS) pour SAP : une solution puissante de composition documentaire, à compléter par un Output Management certifié | Composition documentaire SAP, positionne SEAL en complément d'Adobe Forms |
| 27/04/2026 | Pourquoi le Spool SAP natif ne suffit plus ? | Angle proche de la priorité ScopIOM "spouler les documents" (§5.2) |
| 20/04/2026 | Comment faut-il gérer les impressions et diffusions en entreprise en 2026 ? | Article généraliste gestion des impressions |
| 15/04/2026 | Journée des clients 2026 : Larguez les amarres — Cap sur l'avenir | Événementiel, sans angle SEO direct |

**Bilan de juin 2026** (mois calendaire couvert par le rapport mensuel) : 4 articles publiés (01/06, 08/06, 15/06, 29/06), rythme bimensuel confirmé et inchangé depuis avril. Aucun nouvel empiètement direct sur les priorités ScopIOM restantes n'est apparu en juin (l'article du 13/07 chevauchant la priorité S/4HANA tombe en juillet, déjà journalisé le 17/07/2026).

**Constat (mis à jour le 18/07/2026)** : SEAL Systems avait publié le 13/07/2026 un témoignage client sur le thème S/4HANA. Il s'avère que ScopIOM disposait déjà, au moment de cette veille, de son propre article evergreen sur ce même thème (`/migration-sap-s-4hana-ne-negligez-pas-loutput-management-de-vos-flux-dimpression/`, voir §5.2) : la fenêtre n'était donc pas aussi ouverte qu'estimé initialement — à comparer les deux contenus (angle, structure, Featured Snippet) pour évaluer si l'article ScopIOM tient la comparaison ou nécessite un enrichissement. Rythme de publication SEAL confirmé : environ toutes les 2 semaines depuis avril 2026.

**Re-vérification du 18/07/2026** (rapport mensuel juin 2026) : aucun nouvel article depuis le 13/07/2026 (liste ci-dessus inchangée). Prochain article probable fin juillet/début août compte tenu du rythme observé.

**⚠️ Mise à jour du rapport de force sur "output management system" (requête SERP Semrush live, base FR, re-confirmée le 18/07/2026)** : inchangé depuis le 17/07/2026. **Sefas Innovation (sefasinnovation.fr) occupe la position 1**, SEAL Systems reste en **position 2**. Le §3 et le snapshot du §4.4 (avril 2026) désignaient encore SEAL Systems comme le concurrent en position 1 à battre : cette donnée reste obsolète, l'objectif doit être reformulé en tenant compte de Sefas Innovation en tête. Autre constat confirmé : **mpitech.com (le site corporate de MPI Tech, pas scopiom.com) se positionne en position 7** avec une page `/output-management-systems-guide/`, alors que scopiom.com — le site produit dédié, pivot de toute la stratégie SEO — n'apparaît toujours nulle part dans le top 20 (et n'a toujours aucun mot-clé organique dans la base Semrush FR). Point à examiner avec l'équipe web (risque de dispersion d'autorité entre les deux domaines). Détail complet dans `reports/rapport-mensuel-2026-06.xlsx`, onglet Concurrence.

**Campagne Position Tracking Semrush : correction du 18/07/2026** — contrairement à ce qui était noté ici précédemment ("campagne vide, 0 mot-clé"), une vérification directe a confirmé que la campagne existe et tourne depuis le 13/07/2026 avec 41 mots-clés. Détail complet, liste des mots-clés et limite d'accès API au §5.4 — ne plus utiliser l'ancienne information "campagne vide" nulle part dans ce fichier ni dans les rapports.

---

## 8. Ton éditorial & règles de rédaction

Ces règles s'appliquent à **tout contenu généré** pour ScopIOM, sans exception :

- **Jamais de tiret cadratin (—)** : remplacer par une virgule, deux points, ou un point médian.
- Pas de "conçu pour", "pensé pour", superlatifs non étayés, ou phrasing institutionnel.
- **Double voix éditoriale** : expertise DSI/éditique (concret, orienté problème, orienté bénéfice) + pratique SEO/AEO-GEO de webmaster.
- Langage terrain DSI, citations directes de type témoignage plutôt que copie institutionnelle. Exemples de registre validé :
  - « L'imprimante du site de Lyon est tombée. On a perdu 200 pages. »
  - « Pour retrouver ce document dans les logs, il faut une demi-journée. »
  - « L'auditeur veut la preuve que ce contrat a bien été imprimé le 14 mars. »
- Pas de faux témoignages : si un exemple client est nécessaire et qu'aucun verbatim réel n'est disponible, le signaler explicitement pour remplacement ultérieur par un vrai témoignage.
- Bloc Featured Snippet : moins de 55 mots, positionné avant le premier H2. Vérifier le compte de mots/caractères avant livraison.
- Toujours séparer HTML et CSS dans des fichiers distincts pour l'intégration en module Code Divi. Un composant = un module Code Divi.

---

## 9. Garde-fous d'exactitude produit

À vérifier avant toute affirmation technique publiée :

- **Failover** : trois niveaux distincts — (1) reprise à la page = action manuelle opérateur, (2) failover de groupe d'imprimantes (nouveauté v6) = le job route automatiquement vers une imprimante disponible du groupe, (3) failover d'instance en cluster = reconnexion automatique. Ne jamais confondre ces trois niveaux dans un même paragraphe sans les distinguer.
- **API REST** : ScopIOM dispose d'une API REST documentée permettant la création/modification/suppression de jobs et périphériques, l'intégration dans des outils de supervision tiers (Nagios, Zabbix, Grafana) et l'exposition d'indicateurs opérationnels (jobs en erreur, état du Scheduler, disponibilité des périphériques). Un ancien comparatif interne marque encore ce point "à valider" : cette mention est dépassée, l'API REST est confirmée dans la documentation produit v6.
- **Systèmes d'exploitation supportés** : confirmé par MPI Tech — **Windows Server 2016 / 2019 / 2022 / 2025**, **RHEL 8 / 9 / 10**. (Correction du 17 juillet 2026 : une valeur plus restrictive circulait précédemment, Windows 2016/2019/2022 et RHEL 8/9 uniquement — elle est obsolète, ne plus l'utiliser.)
- **Bases de données supportées** (doc technique v6) : Oracle (19c+, XE compatible), Microsoft SQL Server (2016+, Express et Linux compatibles), PostgreSQL (13+), IBM DB2.
- **Prérequis serveur** : 16 Go RAM minimum, 8 Go disque minimum (installation + données d'usage), quad-core minimum, JDK 17 (inclus à l'installation).
- **Certification SAP BC-XOM** : toute mention doit être vérifiée avec MPI Tech avant publication — ne pas l'affirmer par défaut.
- **ScopTracking™** : produit indépendant, UI et base MongoDB propres. Ne jamais le présenter comme un module de ScopIOM.

---

## 10. Reporting automatisé — cahier des charges

Deux rapports distincts, tous deux au **format .xlsx** (pas de rapport Markdown), envoyés par **email à jda@mpitech.com**.

### 10.1. Rapport hebdomadaire

- **Cadence** : chaque **lundi à 8h00**.
- **Périmètre** : semaine écoulée (lundi-dimanche), comparaison systématique à la semaine précédente (delta en %).
- **Contenu** :
  - **Trafic et audience (GA4)** : sessions, utilisateurs (nouveaux/récurrents), pages vues + top 10 pages, taux de rebond/engagement, durée moyenne d'engagement, répartition géographique (focus France), canaux d'acquisition.
  - **Graphique d'évolution du trafic (nouveau, ajouté le 18/07/2026)** : graphique natif Excel (via `openpyxl.chart`, ex. `LineChart`) dans l'onglet Trafic, montrant les **sessions semaine par semaine sur les 8 dernières semaines calendaires complètes** (lundi-dimanche), pas seulement le delta de la semaine en cours vs précédente. Ne nécessite pas `recalc.py` (le rendu du graphique ne dépend pas du moteur de calcul de formules). **Limite connue** : la propriété GA4 de scopiom.com a été créée le 08/06/2026 — tant que 8 semaines complètes d'historique ne sont pas disponibles, afficher toutes les semaines existantes depuis la création de la propriété plutôt que d'inventer ou d'omettre silencieusement des semaines manquantes, et le signaler dans le rapport.
  - **SEO (Search Console)** : top 20 requêtes (clics, impressions, CTR, position moyenne), nouvelles requêtes apparues, pages en plus forte progression/chute.
  - **Concurrence (SEMrush)** : évolution des mots-clés de la campagne Position Tracking (alerte si mouvement > 3 positions), part de voix si disponible. **Comparatif de visibilité élargi (mise à jour du 18/07/2026)** : ne pas se limiter à SEAL Systems — comparer scopiom.com à **tous les concurrents directs listés au §4.1** (SEAL Systems, Compart, LRS, Sefas, Formpipe/Lasernet, Objectif Lune, Papyrus, OpenText, Quadient, Ricoh, Pitney Bowes, Crawford Technologies) sur le cluster concurrentiel, dans la mesure où Semrush fournit des données pour chacun. Inclure aussi systématiquement **mpitech.com** (le site corporate de l'éditeur) dans ce comparatif, à côté de scopiom.com : le §4.4/§7 a déjà révélé que mpitech.com se positionne mieux que scopiom.com sur au moins un mot-clé prioritaire, ce qui doit être suivi en continu, pas seulement signalé ponctuellement. ⚠️ **Action manuelle requise** : la collecte des positions de la campagne (41+ mots-clés, voir §5.4) n'est pas automatisable via le MCP SEMrush avec l'offre Starter actuelle — quelqu'un doit ouvrir `https://fr.semrush.com/tracking/landscape/30407302_5126938.html` et relever les chiffres à la main (ou via Claude in Chrome sur demande) avant chaque génération de rapport, la Routine planifiée ne peut pas le faire seule.
  - **Veille (§7)** : tout nouvel article détecté sur le blog SEAL Systems dans la semaine.
  - **Alertes automatiques** : chute de trafic > 15 % vs semaine précédente, nouvelle page en erreur 404/500, mot-clé prioritaire sorti du top 10.

### 10.2. Rapport mensuel

- **Cadence** : le **1er jour de chaque mois à 9h00**.
- **Périmètre** : mois calendaire écoulé dans son ensemble (pas une moyenne des rapports hebdo), comparaison au mois précédent **et** au même mois de l'année précédente si l'historique GA4 le permet.
- **Contenu** : mêmes familles d'indicateurs que le rapport hebdomadaire mais en vision mensuelle consolidée, plus :
  - Tendance de fond sur les mots-clés prioritaires du §5.1 et de la campagne Position Tracking (progression/régression sur 30 jours, pas seulement le dernier mouvement).
  - Bilan du mois sur la veille concurrentielle (§7) : liste consolidée des articles SEAL Systems parus dans le mois, avec analyse d'impact le cas échéant.
  - Point d'avancement sur les articles prioritaires en attente (§5.2) : lesquels sont publiés, lesquels restent à faire.
  - Un onglet "Synthèse" en première position du classeur, résumant en 5-6 lignes les faits marquants du mois avant le détail chiffré.
  - **Graphique d'évolution du trafic (nouveau, ajouté le 18/07/2026)** : graphique natif Excel (via `openpyxl.chart`, ex. `LineChart`) dans l'onglet Trafic, montrant les **sessions mois par mois sur les 8 derniers mois calendaires complets**. Ne nécessite pas `recalc.py`. **Limite connue** : la propriété GA4 de scopiom.com a été créée le 08/06/2026, donc à ce stade un seul mois calendaire est entièrement couvert (juin 2026) — afficher tous les mois réellement disponibles depuis la création de la propriété plutôt que d'inventer ou d'omettre silencieusement des points manquants, et le signaler explicitement dans le rapport (le graphique se remplira progressivement au fil des exécutions mensuelles futures).

### 10.3. Format de sortie (.xlsx)

Suivre les conventions de la skill `xlsx` du projet à chaque génération :
- Police professionnelle (Arial), formules réelles plutôt que valeurs figées quand un calcul est en jeu (ex. delta en % = formule, pas un nombre calculé en Python et collé), recalcul via `recalc.py` obligatoire avant tout envoi.
- Un onglet par famille de données (Trafic, SEO, Concurrence, Alertes, + Synthèse pour le mensuel) plutôt qu'un unique onglet surchargé.
- Zéro erreur de formule tolérée avant l'envoi par email.

### 10.4. Diffusion par email — Brevo (décision actée, limite importante découverte)

**Décision** (17 juillet 2026) : l'envoi se fait via **Brevo**, pas via un connecteur Gmail. Raison : Brevo est déjà en service pour scopiom.com (SMTP via WP Mail SMTP), c'est l'outil déjà en place côté MPI Tech pour l'envoi d'emails transactionnels.

- Le connecteur MCP **Brevo est maintenant connecté** côté claude.ai (constat du 17/07/2026, `connector_uuid: d9a4b67a-f7b9-4654-8b3b-c2ec649a79ab`), et attaché aux deux routines cloud (§10.5).
- **Limite importante** : ce connecteur peut **uniquement préparer un brouillon** de campagne email dans Brevo. Il ne peut **jamais envoyer ni programmer un envoi automatiquement** (restriction affichée explicitement dans sa description). Donc même connecté, il ne permet pas un envoi 100 % automatisé : chaque rapport nécessitera une validation manuelle du brouillon dans l'interface Brevo par l'utilisateur.
- **Solution opérationnelle retenue (testée avec succès le 18/07/2026)** : `scripts/send_report_email.py`, script Python local qui envoie le dernier rapport `.xlsx` de `reports/` via l'API transactionnelle Brevo (`POST /v3/smtp/email`, pièce jointe en base64 — contrairement à l'API "campagnes" utilisée par le connecteur MCP, l'API transactionnelle accepte un vrai fichier joint, pas seulement une URL publique). Expéditeur : `webmaster@mpitech.com`. Nécessite `BREVO_API_KEY` dans un fichier `.env` local à la racine du projet (jamais commité, voir `.gitignore`). Premier envoi réel confirmé : `messageId=<202607181053.11194286736@smtp-relay.mailin.fr>`.
  - Usage : `python scripts/send_report_email.py` (envoie le rapport le plus récent à jda@mpitech.com) ou `--file`/`--to` pour surcharger.
  - **Limite** : ce script tourne en local sur la machine de l'utilisateur, pas dans les routines cloud (§10.5) — les environnements cloud n'offrent pas de coffre-fort à secrets (le champ "Variables d'environnement" de claude.ai/code est en clair et explicitement déconseillé pour des identifiants), donc `BREVO_API_KEY` ne peut pas y être stocké sans risque. En pratique : la routine cloud génère et committe le rapport, puis ce script doit être lancé localement (manuellement ou via tâche planifiée Windows) pour l'envoi effectif.
  - Le connecteur MCP Brevo (§10.5) reste utile en complément pour préparer un brouillon visuel dans l'interface Brevo, mais ne remplace pas ce script pour l'envoi automatique.

Python est maintenant installé sur la machine locale (Python 3.12.10 via winget, 18/07/2026) avec `requests`, `python-dotenv`, `openpyxl`. Le blocage noté précédemment est levé.

**Automatisation complète bouclée (18/07/2026)** : deux tâches planifiées Windows relaient les routines cloud pour l'envoi effectif :
- **"ScopIOM - Envoi rapport hebdo"** : chaque lundi 8h45 (45 min après le déclenchement de la routine cloud à 8h, pour lui laisser le temps de terminer).
- **"ScopIOM - Envoi rapport mensuel"** : le 1er de chaque mois à 9h45 (45 min après la routine cloud à 9h).

Chacune exécute `scripts/send_latest_report.ps1`, qui fait `git pull origin master` (récupère le rapport que la routine cloud vient de committer) puis lance `scripts/send_report_email.py`. Logs dans `logs/` (non versionné). **Limite à connaître** : ces tâches planifiées ne s'exécutent que si la machine Windows de l'utilisateur est allumée et la session ouverte à l'heure prévue — ce n'est pas une automatisation cloud-to-cloud, le PC local reste un maillon de la chaîne tant que les routines cloud n'ont pas de coffre-fort à secrets.

### 10.4bis. Chiffrement des clés API au repos (18/07/2026)

`.env` (clés Brevo, Semrush) est exclu de git par `.gitignore` et n'a jamais été commité. En complément, une copie chiffrée `.env.encrypted` **est commitée** dans le dépôt via `scripts/vault.py` (bibliothèque `cryptography`, chiffrement symétrique Fernet) :
- `python scripts/vault.py encrypt` : chiffre `.env` → `.env.encrypted`. Génère une clé de chiffrement si elle n'existe pas encore, stockée **délibérément en dehors du dépôt** dans `C:\Users\Julien\.scopiom-vault.key` (jamais commitée, jamais poussée).
- `python scripts/vault.py decrypt` : restaure `.env` depuis `.env.encrypted` (utile sur une nouvelle machine, à condition d'avoir une copie de sauvegarde de la clé).
- **Ce que ça protège** : une fuite ou un accès non autorisé au dépôt GitHub (repo rendu public par erreur, clone non autorisé) ne donne accès à aucune clé en clair.
- **Ce que ça NE change PAS** : les routines cloud (§10.5) n'ont toujours pas accès à ces clés — ni en clair ni chiffrées, puisqu'elles n'ont ni le fichier `.env` ni la clé de déchiffrement externe au dépôt. C'est une amélioration de sécurité pour les scripts locaux (envoi email, test API), pas une solution au problème d'automatisation cloud du §5.4 (Position Tracking) — les deux sujets sont indépendants, volontairement non mélangés après discussion avec l'utilisateur le 18/07/2026.

### 10.5bis. Optimisations de temps d'exécution (18/07/2026)

Les deux premiers tests réels (§10.5) ont pris environ 20-30 minutes chacun. Deux causes identifiées et corrigées :
- **`recalc.py`/LibreOffice** : bloquait jusqu'à ~20-24 min (3 tentatives × 8 min dans le pire cas). Les prompts des deux routines limitent maintenant cette étape à **1 seule tentative, 2-3 minutes maximum**, sans retry — les formules restent standard et se calculent normalement à l'ouverture dans Excel/Sheets de toute façon.
- **Réinstallation des paquets Python à chaque session** (`pip install requests python-dotenv openpyxl pandas`, ~30-60s perdus à chaque fois) : déplacée dans le **script de configuration** de l'environnement cloud "ScopIOM" (exécuté une fois au démarrage de la session, avant le lancement de Claude Code), donc les paquets sont déjà prêts quand la routine commence à travailler.

Ces deux changements devraient ramener une exécution normale à ~5-10 minutes. À vérifier lors des prochaines exécutions réelles (prochaine hebdo : lundi 20/07, prochaine mensuelle : 1er août).

### 10.5. Automatisation (Claude Code Routines) — mise en place le 17/07/2026

Deux routines cloud créées via `/schedule`, chacune clonant le dépôt GitHub `https://github.com/hemanaco72/scopiom-reporting` (environnement cloud "ScopIOM") à chaque exécution :

| Routine | Cron (UTC) | Heure locale visée (Paris) | ID |
|---|---|---|---|
| Rapport hebdo ScopIOM | `0 6 * * 1` (chaque lundi) | 8h00 (calé sur l'heure d'été CEST) | `trig_01RAqxSkx5HxEmxh157foV5J` |
| Rapport mensuel ScopIOM | `0 7 1 * *` (1er du mois) | 9h00 (calé sur l'heure d'été CEST) | `trig_01HphsuxMJMhfb1UfLBxmKFi` |

⚠️ **Le cron est fixe en UTC** : calé sur l'heure d'été. En heure d'hiver (CET, UTC+1), les rapports partiront avec 1h de décalage (9h/10h Paris au lieu de 8h/9h) tant que le cron n'est pas réajusté manuellement à l'automne.

**Connecteurs MCP attachés aux deux routines (mise à jour du 17/07/2026 au soir)** : `Semrush`, `Notion`, `Composio` (`connector_uuid: 5cab6eb4-9e18-4022-a2c7-f3557db74c55`, connecteur personnalisé ajouté via `https://connect.composio.dev/mcp`, authentifié en tant que `webmaster@mpitech.com`), `Brevo` (`connector_uuid: d9a4b67a-f7b9-4654-8b3b-c2ec649a79ab`, voir limite d'envoi au §10.4).

**GA4 et Search Console n'ont pas de connecteur natif dans le répertoire claude.ai** (recherche confirmée le 17/07/2026 : rien en cherchant "Google Analytics" ni "Search Console", seuls des agrégateurs tiers payants comme Supermetrics ou Windsor.ai ressortent). La voie retenue est de passer par **Composio**, une plateforme d'intégrations qui peut exposer des toolkits Google Analytics/Search Console une fois configurés côté Composio. **Composio est connecté côté claude.ai, mais il reste à vérifier/configurer dans le dashboard Composio (dashboard.composio.dev) que les toolkits Google Analytics Data API et Search Console sont bien activés et liés au compte Google utilisé pour scopiom.com** — cette étape n'a pas été faite à date, se contenter de la connexion du connecteur ne garantit pas que ces outils précis soient disponibles. Chaque routine vérifie les outils disponibles au démarrage et signale leur absence plutôt que d'inventer des données.

Chaque routine lit `CLAUDE.md` en entier au démarrage, fait la veille SEAL Systems (§7) et met à jour cette section, tente un `.xlsx` (bascule en Markdown de repli si Python/openpyxl indisponible dans l'environnement cloud — voir blocage Python noté plus haut, propre à la machine locale, pas forcément à l'environnement cloud), committe le rapport dans `reports/` sur `master`, tente l'envoi Brevo, et termine toujours par un résumé explicite de ce qui a été sauté et pourquoi plutôt que d'échouer silencieusement.

Gérer les routines : https://claude.ai/code/routines (liste, activation/désactivation, exécution manuelle ; la suppression n'est possible que depuis cette page web).

---

## 11. Ressources internes disponibles

- `Comparatif_Enterprise_Output_Management.md` : comparatif fonctionnel détaillé (base du §4.2).
- `CR_Projet_ScopIOM-1.docx` : compte-rendu projet, stratégie SEO Semrush initiale, charte graphique, architecture du site.
- `ScopIOM_v6_ReleaseNotes(.docx / _EN.docx)`, `Overview_-_ScopIOM_6_0.docx`, `Survol_fonctionnel_-_ScopIOM_6.docx` : documentation produit v6 de référence pour toute affirmation technique.
- `scoptrackingsurvol1_4.pdf` : documentation fonctionnelle ScopTracking v1.4.
- `qr.xlsx` : questionnaire RFI/RFP client (DB Schenker) avec réponses produit détaillées — source fiable pour les capacités techniques réellement démontrées (protocoles supportés, follow-me-print, licensing, HA).

---

*Dernière consolidation : juillet 2026. Ce fichier doit être mis à jour à chaque nouvelle donnée Semrush, chaque évolution produit v6.x, ou chaque changement de règle éditoriale.*
