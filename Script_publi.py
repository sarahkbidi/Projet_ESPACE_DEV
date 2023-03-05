# -*- coding: utf-8 -*-
"""
Created on Sun Mar  5 18:33:36 2023

@author: sarah
"""

# Import des modules utils au script
import requests # Importer le module requests pour effectuer des requêtes HTTP
from bs4 import BeautifulSoup  # Importer le module BeautifulSoup pour extraire des données HTML
import csv # Importer le module csv pour écrire les données dans un fichier csv

#URL de la page de recherche des publications de l'année 2022 et de l'unité de recherche UMR 228 Espace-Dev
url = "https://hal.science/ESPACE-DEV"

response = requests.get(url) # Envoyer une requête GET à l'URL et récupérer la réponse
soup = BeautifulSoup(response.text, "html.parser") # Analyser le HTML de la réponse avec BeautifulSoup

# Extraire les détails de toutes les publications en cherchant les balises div avec la classe "doc_result"
publications = soup.find_all("div", class_="doc_result")

# Créer un fichier CSV et écrire les entêtes de colonnes
with open('publications.csv', mode='w') as csv_file:
    fieldnames = ['Title', 'Authors', 'Publication Type', 'Publication Site', 'PDF Link'] # Nom des colonnes
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()

    # Parcourir toutes les publications et extraire les informations pertinentes
    for pub in publications:
        title = pub.find("h2", class_="doc_title").text.strip()
        authors = pub.find("div", class_="doc_authors").text.strip()
        pub_type = pub.find("div", class_="doc_type").text.strip()
        pub_site = pub.find("div", class_="doc_site").text.strip()
        pdf_link = pub.find("a", class_="btn btn-default btn-xs btn-round").get("href")

         # Écrire les informations de la publication dans le fichier CSV
        writer.writerow({'Titre': title, 'Auteurs UMR': authors, 'Type de Publication ': pub_type, 'Site étude': pub_site, 'PDF accessible ?': pdf_link})
