import os
import shutil
import pandas as pd

# Charger le fichier Excel
df = pd.read_excel('/Users/philippeprince/Documents/GitHub/data-exploration-for-social-science/3_sentiment_classified_GS.xlsx')

# Trier le dataframe selon 'average_score' dans l'ordre décroissant
df = df.sort_values('average_score', ascending=False)

# Récupérer les noms de fichiers et les scores moyens
names = df['name'].tolist()
scores = df['average_score'].tolist()

# Parcourir les noms de fichiers et renommer chaque fichier
folder = '/Users/philippeprince/Documents/GitHub/data-exploration-for-social-science/src/GS_copy/'

for i, name in enumerate(names):
    src = folder + name

    # Séparez le nom du fichier de son extension
    basename, extension = os.path.splitext(name)

    # Tronquez le nom du fichier s'il dépasse 95 caractères (en laissant de la place pour l'index et l'extension)
    short_name = (basename[:92] + '...') if len(basename) > 95 else basename
    dst = folder + f'{i}_{short_name}{extension}'

    # Renomme le fichier
    os.rename(src, dst)

print("Opération terminée.")