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

**Dépasser SEAL Systems sur "output management system"** (marché français). C'est le mot-clé prioritaire absolu.

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

### 4.4. Snapshot SERP le plus récent (analyse Semrush, avril 2026)

| Concurrent | Position sur "output management system" | Trafic mensuel estimé |
|---|---|---|
| SEAL Systems | 1 | 218 visites/mois |
| LRS | 5 | 21 visites/mois |
| Compart | 7 | 16 visites/mois |
| ScopIOM | absent | objectif : top 3 |

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

| Article | KD | Note |
|---|---|---|
| Migration SAP S/4HANA et output management | 8 | **Priorité n°1 actuelle** |
| Output Management : définition, fonctionnement, cas d'usage DSI | 18 | 880/mois, vise à dépasser SEAL Systems |
| Print vs. Output management | 12 | SEAL présent mais contenu faible |
| Comment centraliser la gestion des impressions multisites | 9 | Featured Snippet libre |
| Failover imprimante / haute disponibilité | 14 | Featured Snippet libre |
| Spouler les documents | 27 | Featured Snippet libre |

### 5.3. Mapping H1 par page parente

| Page | H1 cible |
|---|---|
| Homepage | Vos flux documentaires sous contrôle, de l'entrée à la sortie |
| Solution | ScopIOM — logiciel d'Output Management et d'ordonnancement de flux éditiques |
| Fonctionnalités | Toutes les fonctionnalités ScopIOM pour gérer vos flux d'impression et vos documents |
| Cas d'usage | Comment centraliser la gestion de vos impressions et flux documentaires |
| Ressources | Output Management — définitions, guides et FAQ pour les DSI |

### 5.4. Campagne de suivi en direct (SEMrush Position Tracking)

Une campagne active suit **34 mots-clés répartis en 6 clusters** : générique, concurrentiel, fonctionnalités, secteurs, intégrations techniques, conformité/souveraineté. Concurrents suivis : SEAL Systems, Compart, LRS, OpenText, Quadient, Ricoh, Crawford Technologies.

**Ne pas recopier une liste figée de ces 34 mots-clés dans ce fichier** : elle évolue. Le rapport hebdomadaire doit interroger cette campagne en direct via le MCP SEMrush (`position_tracking`) pour avoir les positions à jour.

Une deuxième campagne est prévue avec ChatGPT comme moteur de recherche, pour comparer visibilité SEO classique et visibilité IA (voir §6).

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
  - **SEO (Search Console)** : top 20 requêtes (clics, impressions, CTR, position moyenne), nouvelles requêtes apparues, pages en plus forte progression/chute.
  - **Concurrence (SEMrush)** : évolution des mots-clés de la campagne Position Tracking (alerte si mouvement > 3 positions), comparatif de visibilité vs SEAL Systems sur le cluster concurrentiel, part de voix si disponible.
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

### 10.3. Format de sortie (.xlsx)

Suivre les conventions de la skill `xlsx` du projet à chaque génération :
- Police professionnelle (Arial), formules réelles plutôt que valeurs figées quand un calcul est en jeu (ex. delta en % = formule, pas un nombre calculé en Python et collé), recalcul via `recalc.py` obligatoire avant tout envoi.
- Un onglet par famille de données (Trafic, SEO, Concurrence, Alertes, + Synthèse pour le mensuel) plutôt qu'un unique onglet surchargé.
- Zéro erreur de formule tolérée avant l'envoi par email.

### 10.4. Diffusion par email — prérequis technique restant

L'envoi automatique vers jda@mpitech.com nécessite un moyen d'envoi configuré dans Claude Code, **pas encore mis en place à ce stade** :
- **Option recommandée** : connecteur MCP Gmail ajouté à Claude Code (`claude mcp add`, authentification OAuth au compte Google déjà utilisé pour GA4/Search Console).
- **Alternative** : script Python utilisant le SMTP Brevo (déjà en service pour le site scopiom.com) avec une clé API Brevo dédiée à ce projet, séparée de celle de WordPress.

Tant que ce point n'est pas réglé, toute Routine planifiée peut générer le fichier `.xlsx` mais échouera à l'envoyer : à traiter avant la première exécution automatique réelle.

### 10.5. Automatisation (Claude Code Routines)

Deux routines séparées (cadences différentes) :
```
/schedule
```
puis décrire précisément la tâche pour chacune, en indiquant explicitement le jour/heure, le format .xlsx, la génération via les MCP `ga4`/`search-console`/`semrush`, et l'envoi à jda@mpitech.com. Nommer les routines distinctement (ex. "Rapport hebdo ScopIOM" / "Rapport mensuel ScopIOM") pour éviter toute confusion dans `/schedule list`.

**Connecteurs MCP attendus dans ce projet Claude Code** : `ga4` (Google Analytics Data/Admin API), `search-console`, `semrush`, et un connecteur d'envoi d'email (Gmail ou équivalent, voir §10.4). Vérifier leur présence avec `claude mcp list` avant de lancer une génération de rapport.

---

## 11. Ressources internes disponibles

- `Comparatif_Enterprise_Output_Management.md` : comparatif fonctionnel détaillé (base du §4.2).
- `CR_Projet_ScopIOM-1.docx` : compte-rendu projet, stratégie SEO Semrush initiale, charte graphique, architecture du site.
- `ScopIOM_v6_ReleaseNotes(.docx / _EN.docx)`, `Overview_-_ScopIOM_6_0.docx`, `Survol_fonctionnel_-_ScopIOM_6.docx` : documentation produit v6 de référence pour toute affirmation technique.
- `scoptrackingsurvol1_4.pdf` : documentation fonctionnelle ScopTracking v1.4.
- `qr.xlsx` : questionnaire RFI/RFP client (DB Schenker) avec réponses produit détaillées — source fiable pour les capacités techniques réellement démontrées (protocoles supportés, follow-me-print, licensing, HA).

---

*Dernière consolidation : juillet 2026. Ce fichier doit être mis à jour à chaque nouvelle donnée Semrush, chaque évolution produit v6.x, ou chaque changement de règle éditoriale.*
