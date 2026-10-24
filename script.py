# Importing pandas and matplotlib
import pandas as pd
import matplotlib.pyplot as plt

# Read in the Netflix CSV as a DataFrame
netflix_df = pd.read_csv(r"C:\Users\farez\Downloads\netflix_data.csv")

print(netflix_df.head(8))
# 2. Vérifier les noms de colonnes disponibles (bon réflexe de debug)
print(netflix_df.columns.tolist())

# 3. Filtrer les lignes où le type est 'Movie'
#    -> netflix_df["type"] == "Movie" crée un masque booléen (True/False)
#    -> netflix_df[masque] garde uniquement les lignes True, toutes colonnes conservées
netflix_movies = netflix_df[netflix_df["type"] == "Movie"]

# 4. Vérifier que le filtre a fonctionné : ne doit afficher que ['Movie']
print("Valeurs uniques dans 'type' :", netflix_movies["type"].unique())

# 5. Isoler les films sortis en 1990 (colonne release_year = année de sortie, valeur numérique)
netflix_1990_release = netflix_movies[netflix_movies["release_year"] == 1990]
print(netflix_1990_release)

plt.hist(netflix_1990_release["duration"])
plt.xlabel("Durée (minutes)")
plt.ylabel("Fréquence")
plt.title("Distribution des durées de films")
plt.show()

duration = 100
short_movie_count = 7

# Correction:
# - Use '==' for comparison, not '=' (which is assignment)
# - Add '&' between all conditions
# - Parentheses around each condition for correct operator precedence

short_action_1990s = netflix_movies[
    (netflix_movies["release_year"] == 1990) &
    (netflix_movies["genre"].str.contains("Action", na=False)) &
    (netflix_movies["duration"] < 90)
]

print(short_action_1990s)

# Compter le nombre de lignes = nombre de films correspondants
short_movie_count = len(short_action_1990s)
print("Nombre de films d'action courts des années 1990 :", short_movie_count)


# Étape 1 : uniquement les films (déjà fait)
print("Films total :", len(netflix_movies))

# Étape 2 : + décennie 1990s
step2 = netflix_movies[(netflix_movies["release_year"] >= 1990) & (netflix_movies["release_year"] < 2000)]
print("Après filtre décennie :", len(step2))

# Étape 3 : + genre Action
step3 = step2[step2["genre"] == "Action"]  # essaie == d'abord, pas contains
print("Après filtre genre :", len(step3))

# Étape 4 : + durée < 90
step4 = step3[step3["duration"] < 90]
print("Après filtre durée :", len(step4))

short_movie_count = len(step4)
print("Résultat final :", short_movie_count)