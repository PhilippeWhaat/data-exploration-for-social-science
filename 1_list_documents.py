import os
from openpyxl import Workbook

# Get the directory of the current script
script_directory = os.path.dirname(os.path.abspath(__file__))

source = '_vLex'
# Construct the PDF directory path relative to the script's directory
pdf_directory = os.path.join(script_directory, f"src/{source}")

# Créer un nouveau classeur Excel
wb = Workbook()
ws = wb.active

# Écrire le nom des fichiers PDF dans la première colonne
for filename in os.listdir(pdf_directory):
    if filename.endswith(".pdf"):
        ws.append([filename])

# Enregistrer le fichier Excel
excel_filename = os.path.join(pdf_directory, f"liste_fichiers{source}.xlsx")
wb.save(excel_filename)