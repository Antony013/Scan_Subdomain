# Scan_Subdomain

A partir d'une liste de sous domaine les plus utilisés, scan de sous domaine à partir d'un nom de domaine donné.

_________________

Options :

-h, --help Montrer les options
<br>
<code> python scan_sous_domaine.py -h </code>

-d DOMAIN, --domain Nom du domaine - google.com par défaut
<br>
<code> python scan_sous_domaine.py -d google.com </code>

-f FILE, --file Liste de sous domaine - liste_scan_sous_domaine.txt par défaut
<br>
<code> python scan_sous_domaine.py -f liste_scan_sous_domaine.txt </code>

_________________

Exemples :

<code> python scan_sous_domaine.py </code>
> Sous domaine trouvé : https://www.google.com
>
> Sous domaine trouvé : https://mail.google.com
>
> Sous domaine trouvé : https://m.google.com
>
> Sous domaine trouvé : https://blog.google.com
>
> Sous domaine trouvé : https://admin.google.com
>
> Sous domaine trouvé : https://news.google.com
>
> ...
