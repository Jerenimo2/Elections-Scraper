Elections Scraper 3 projekt Engeto


Popis projektu
Tento projekt slouží k extrahování výsledků z parlamentních voleb v roce 2017.
Odkaz k prohlédnutí najdete zde https://volby.cz/pls/ps2017nss/ps3?xjazyk=CZ



Instalace knihoven

Knihovny, které jsou použity v kódu jsou uložené v souboru requirements.txt
Pro instalaci doporučuji použít nové virtuální prostředí:
pip3 install -r requirements.txt       # instalace knihoven
pip3 --version                         # ověřím verzi manageru



Spuštění projektu

Spuštění projektu Elections Scraper.py v rámci příkazového řádku požaduje dva argumenty.
 python elections-scraper <odkaz-uzemniho-celku> <vysledny-soubor>
Následně se vám stáhnou výsledky jako soubor s příponou .csv .



Ukázka projektu

Výsledky hlasování pro okres Benešov:
1. argument: https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2101
2. argument: vysledky_benesov.csv

Spuštění programu:
 python Elections Scraper.py "https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2101"

Průběh stahování:
 STAHUJI DATA Z VYBRANEHO URL: https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2101
 UKLADAM DO SOUBORU: vysledky_benesov.csv
 UKONCUJI ELECTION SCRAPER

