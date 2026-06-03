import urllib.request
import xml.etree.ElementTree as ET
import ssl
import sys

sys.stdout.reconfigure(encoding='utf-8')
context = ssl._create_unverified_context()

feeds = {
    'CTI': 'https://www.cert.ssi.gouv.fr/cti/feed/',
    'ALERTE': 'https://www.cert.ssi.gouv.fr/alerte/feed/',
    'AVIS': 'https://www.cert.ssi.gouv.fr/avis/feed/',
    'ACTUALITE': 'https://www.cert.ssi.gouv.fr/actualite/feed/'
}

with open('cert_fr_articles.txt', 'w', encoding='utf-8') as f:
    for name, url in feeds.items():
        f.write(f"\n=== {name} ===\n")
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req, context=context) as response:
                root = ET.fromstring(response.read())
                for item in root.findall('./channel/item')[:30]:
                    title = item.find('title').text
                    link = item.find('link').text
                    pubDate = item.find('pubDate').text if item.find('pubDate') is not None else ''
                    f.write(f"- {title}\n  URL: {link}\n  Date: {pubDate}\n")
        except Exception as e:
            f.write(f"Error fetching {name}: {e}\n")
print("Done writing to cert_fr_articles.txt")
