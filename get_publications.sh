#!/bin/bash

# Définition des variables
QUERY='https://hal.science/ESPACE-DEV/search/index/?q=producedDateY_i%3A2022&rows=30&submitType_s=notice+OR+file+OR+annex&labStructName_t=UMR+228+Espace-Dev%2C+Espace+pour+le+d%C3%A9veloppement&producedDateY_i=2022'
TEMP_FILE='temp.json'
OUTPUT_FILE='publications.csv'

# Récupération des données depuis HAL
curl -s $QUERY | jq '.response.docs[] | {title: .title_s, type: .docType_s, author: .authFullName_s, site: .strAffiliation_s}' > $TEMP_FILE

# Conversion du ficher JSON en 
# Conversion du fichier JSON en CSV avec Pandoc
# pandoc $TEMP_FILE -s -o $OUTPUT_FILE --csv

jq -r '[.[] | @csv]' temp.json > publication.csv

# Suppression du fichier temporaire
#rm $TEMP_FILE
