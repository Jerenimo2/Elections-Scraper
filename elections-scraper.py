"""
projekt_3.py: třetí projekt do Engeto Online Python Akademie

author: Jan Kýr
email: jerenimo@seznam.cz
discord: Jan K.
"""

#https://volby.cz/pls/ps2017nss/ps3?xjazyk=CZ

#venv\Scripts\activate.bat

#cd "C:\Users\Jerenimo\OneDrive\Desktop\IT rekvalifikace\Engeto 3 projekt"


import requests
from bs4 import BeautifulSoup
import csv
import sys

def scrape_election_results(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    results_table = soup.find('table', {'id': 'ps311_t1'})
    rows = results_table.find_all('tr')[2:]  # přeskočit hlavičku tabulky

    results = []
    for row in rows:
        cols = row.find_all('td')
        obec_code = cols[0].text.strip()
        obec_name = cols[1].text.strip()
        voters = cols[3].text.strip()
        envelopes = cols[4].text.strip()
        valid_votes = cols[7].text.strip()
        # Předpokládáme, že strany jsou v dalších sloupcích, začínající od indexu 11
        parties_votes = [col.text.strip() for col in cols[11:]]

        results.append([obec_code, obec_name, voters, envelopes, valid_votes] + parties_votes)

    return results

def save_to_csv(data, filename):
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Kód obce', 'Název obce', 'Voliči v seznamu', 'Vydáné obálky', 'Platné hlasy'] + ['Strana ' + str(i + 1) for i in range(len(data[0]) - 5)])
        writer.writerows(data)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Chyba: Program vyžaduje dva argumenty: URL adresu a název výstupního souboru CSV.")
        sys.exit(1)

    url = sys.argv[1]
    filename = sys.argv[2]

    try:
        print(f"STAHUJI DATA Z VYBRANEHO URL: {url}")
        results = scrape_election_results(url)
        print(f"UKLADAM DO SOUBORU: {filename}")
        save_to_csv(results, filename)
        print(f"UKONCUJI ELECTION SCRAPER")
    except Exception as e:
        print(f"Chyba při zpracování: {e}")
