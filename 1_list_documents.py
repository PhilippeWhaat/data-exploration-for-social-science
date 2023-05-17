import os
from openpyxl import Workbook

# Répertoire contenant les fichiers PDF
pdf_directory = "src/google_scholar"

# Créer un nouveau classeur Excel
wb = Workbook()
ws = wb.active

# Écrire le nom des fichiers PDF dans la première colonne
for filename in os.listdir(pdf_directory):
    if filename.endswith(".pdf"):
        ws.append([filename])

# Enregistrer le fichier Excel
excel_filename = "liste_fichiers.xlsx"
wb.save(excel_filename)