import requests
from argparse import ArgumentParser
import datetime

parser = ArgumentParser(
    prog='Scan de sous domaine.',
    description='A partir d\'une liste de sous domaine les plus utilisés, scan de sous domaine à partir d\'un nom de domaine donné.'
)

parser.add_argument("-d", "--domain", default="google.com",
                    help="Nom du domaine", type=str)
parser.add_argument("-f", "--file", default="liste_scan_sous_domaine.txt",
                    help="Liste de sous domaine", type=str)

args = parser.parse_args()

# liste des sous domaines les plus populaires
file = open(args.file)
content = file.read()
subdomains = content.splitlines()

# liste des sous domaines découvert
subdomain_find = []

for subdomain in subdomains:
    url = f"https://{subdomain}.{args.domain}"
    # on test si il y a une erreur c'est que le sous domaine n'existe pas
    try:
        requests.get(url)
    except requests.ConnectionError:
        # si il n'y a pas de sous domaines on pass
        pass
    else:
        print("Sous domaine trouvé :", url)
        # on ajoute le sous domaines trouvé dans la liste
        subdomain_find.append(url)

# on crée un doc
# with open(f"sous_domaine_trouve_pour_{args.domain}_{datetime.datetime.today().strftime('%Y_%m_%d')}.txt", "w") as f:
with open(f"sous_domaine_trouve_pour_{args.domain}.txt", "w") as f:
    for subdomain in subdomain_find:
        print(subdomain, file=f)
