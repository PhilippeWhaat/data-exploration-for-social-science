import os
import pandas as pd


# Get the directory of the current script
script_directory = os.path.dirname(os.path.abspath(__file__))

source = 'WHOLE'
# Construct the PDF directory path relative to the script's directory
df = pd.read_excel(os.path.join(script_directory, f"3_sentiment_classified_{source}.xlsx"))

# Trier le dataframe selon 'average_score' dans l'ordre décroissant
df = df.sort_values('average_score_ND', ascending=False)

# Récupérer les noms de fichiers et les scores moyens
names = df['name'].tolist()
scores = df['average_score_ND'].tolist()

# Parcourir les noms de fichiers et renommer chaque fichier
folder = f'/Users/philippeprince/Documents/GitHub/data-exploration-for-social-science/src/{source}/'

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