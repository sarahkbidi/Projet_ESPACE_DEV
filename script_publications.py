# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 21:24:13 2023

@author: sarah
"""

import requests
import csv

# Paramètres de la requête de recherche
base_url = '//api.archives-ouvertes.fr/search/ESPACE-DEV/'
params = {
    'q': 'labStructId_s:196623',  # ID du laboratoire à rechercher ou nom labStructName_t : UMR 228 Espace-De
    'wt': 'json',  # Format de sortie des résultats
    'rows': 30,  # Nombre de résultats par page
    'sort': 'producedDateY_i desc'  # Tri des résultats par date décroissante
}

# Effectuer la requête de recherche
response = requests.get(base_url, params=params)

# Extraire les données des publications depuis les résultats de recherche
publications = []
for doc in response.json()['response']['docs']:
    title = doc.get('title_s', '')
    authors = doc.get('authFullName_s', [])
    pub_type = doc.get('docType_s', '')
    pdf_link = doc.get('fileMain_s', '')

    # Ajouter les données de la publication à la liste
    publications.append({'title': title, 'authors': authors, 'type': pub_type, 'pdf_link': pdf_link})

# Écrire les données dans un fichier CSV
with open('publications.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['Titre', 'Auteurs UMR', 'Type de publications', 'PDF accessible ?']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for pub in publications:
        writer.writerow(pub)
