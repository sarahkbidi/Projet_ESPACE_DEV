import requests
import json
import csv

# Définition des variables
QUERY = 'https://hal.science/ESPACE-DEV/search/index/?q=producedDateY_i%3A2022&rows=30&submitType_s=notice+OR+file+OR+annex&labStructName_t=UMR+228+Espace-Dev%2C+Espace+pour+le+d%C3%A9veloppement&producedDateY_i=2022'
TEMP_FILE = 'temp.json'
OUTPUT_FILE = 'publications.csv'

# Récupération des données depuis HAL
response = requests.get(QUERY)
json_data = response.json()
results = json_data['response']['docs']

# Extraction des champs
extracted_data = []
for result in results:
    extracted_data.append({
        'title': result['title_s'],
        'type': result['docType_s'],
        'author': result['authFullName_s'],
        'site': result['strAffiliation_s']
    })

# Stockage des données dans un fichier temporaire en JSON
with open(TEMP_FILE, 'w') as f:
    json.dump(extracted_data, f)

# Conversion du fichier JSON en CSV
with open(TEMP_FILE, 'r') as f:
    json_data = json.load(f)
    csv_data = csv.writer(open(OUTPUT_FILE, 'w'))
    header = ['title', 'type', 'author', 'site']
    csv_data.writerow(header)
    for item in json_data:
        csv_data.writerow([item['title'], item['type'], item['author'], item['site']])
        
# Suppression du fichier temporaire
# import os
# os.remove(TEMP_FILE)

