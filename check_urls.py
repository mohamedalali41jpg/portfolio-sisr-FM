import urllib.request
import ssl

context = ssl._create_unverified_context()

# All candidate URLs to test - organized by month
candidates = [
    # === DECEMBRE 2025 - La Poste DDoS ===
    ("Dec25-LaPoste", "https://www.lemondeinformatique.fr/actualites/lire-la-poste-touchee-par-une-attaque-ddos-d-ampleur-inedite-en-france-96123.html"),
    ("Dec25-LaPoste", "https://www.developpez.com/actu/363891/La-Poste-victime-d-une-cyberattaque-DDoS-majeure-revendiquee-par-le-groupe-pro-russe-NoName057/"),
    ("Dec25-LaPoste", "https://www.01net.com/actualites/la-poste-victime-cyberattaque-ddos-hackers-prorusses.html"),
    ("Dec25-LaPoste", "https://www.clubic.com/actualite-546123-la-poste-victime-d-une-cyberattaque-ddos-massive.html"),
    
    # === JANVIER 2026 - FICOBA ===
    ("Jan26-FICOBA", "https://www.01net.com/actualites/ficoba-fuite-donnees-bancaires-1-2-million-comptes.html"),
    ("Jan26-FICOBA", "https://www.developpez.com/actu/364567/FICOBA-piratage-1-2-million-comptes-bancaires-exposes/"),
    ("Jan26-FICOBA", "https://www.lemondeinformatique.fr/actualites/lire-ficoba-des-acces-illegitimes-a-1-2-million-de-comptes-bancaires-96456.html"),
    
    # === FEVRIER 2026 - Cegedim Sante ===
    ("Fev26-Cegedim", "https://www.lemondeinformatique.fr/actualites/lire-cegedim-sante-piratage-15-millions-patients-96789.html"),
    ("Fev26-Cegedim", "https://www.developpez.com/actu/365123/Cegedim-Sante-piratage-15-millions-patients-donnees-medicales/"),
    ("Fev26-Cegedim", "https://www.01net.com/actualites/cegedim-sante-piratage-donnees-15-millions-patients.html"),
    ("Fev26-Cegedim", "https://lemagit.fr/actualites/366623123/Cegedim-Sante-ce-que-lon-sait-de-la-fuite-de-donnees"),
    
    # === MARS 2026 - CNOUS ===
    ("Mar26-CNOUS", "https://www.lemondeinformatique.fr/actualites/lire-cyberattaque-cnous-770-000-etudiants-concernes-96890.html"),
    ("Mar26-CNOUS", "https://www.developpez.com/actu/365456/CNOUS-774-000-etudiants-touches-par-une-fuite-de-donnees/"),
    ("Mar26-CNOUS", "https://www.numerama.com/cyberguerre/cnous-piratage-774000-etudiants.html"),
    
    # === AVRIL 2026 - ANTS ===
    ("Avr26-ANTS", "https://www.developpez.com/actu/365637/France-Titres-ANTS-victime-d-un-piratage-massif-les-donnees-personnelles-de-11-7-millions-de-Francais-exposees-un-adolescent-de-15-ans-interpelle/"),
    ("Avr26-ANTS", "https://www.lemondeinformatique.fr/actualites/lire-piratage-ants-france-titres-11-millions-francais-97123.html"),
    ("Avr26-ANTS", "https://www.01net.com/actualites/piratage-ants-france-titres-11-millions-francais.html"),
    
    # === MAI 2026 - Almerys ===
    ("Mai26-Almerys", "https://www.lemondeinformatique.fr/actualites/lire-almerys-piratage-15-millions-numeros-securite-sociale-97456.html"),
    ("Mai26-Almerys", "https://www.developpez.com/actu/366123/Almerys-piratage-15-millions-numeros-securite-sociale/"),
    ("Mai26-Almerys", "https://www.01net.com/actualites/almerys-piratage-securite-sociale-15-millions.html"),
]

print("Testing all candidate URLs...\n")
for label, url in candidates:
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'})
        res = urllib.request.urlopen(req, context=context, timeout=8)
        print(f"OK {res.getcode()}: [{label}] {url}")
    except Exception as e:
        code = getattr(e, 'code', str(e)[:50])
        print(f"FAIL {code}: [{label}] {url}")
