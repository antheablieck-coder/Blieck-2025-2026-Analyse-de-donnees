#coding:utf8

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats
import math

#Fonction pour ouvrir les fichiers
def ouvrirUnFichier(nom):
    contenu = pd.read_csv(nom, encoding="utf-8", sep=",", low_memory=False)# Modification de la fonction suite a des problèmes de format
    return contenu

#Fonction pour convertir les données en données logarithmiques
def conversionLog(liste):
    log = []
    for element in liste:
        log.append(math.log(element))
    return log

#Fonction pour trier par ordre décroissant les listes (îles et populations)
def ordreDecroissant(liste):
    liste.sort(reverse=True)
    return liste

#Fonction pour obtenir le classement des listes spécifiques aux populations
def ordrePopulation(pop, etat):
    ordrepop = []
    for element in range(len(pop)):
        if np.isnan(pop[element]) == False:
            ordrepop.append([float(pop[element]), etat[element]])
    ordrepop = ordreDecroissant(ordrepop)
    for element in range(len(ordrepop)):
        ordrepop[element] = [element + 1, ordrepop[element][1]]
    return ordrepop

#Fonction pour obtenir l'ordre défini entre deux classements (listes spécifiques aux populations)
def classementPays(ordre1, ordre2):
    classement = []
    for element1 in range(len(ordre1)):
        for element2 in range(len(ordre2)):
            if ordre1[element1][1] == ordre2[element2][1]:
                classement.append([ordre1[element1][0], ordre2[element2][0]])
    return classement


# ===================
# Partie sur les îles
# ===================

iles = ouvrirUnFichier("./data/island-index.csv")

# Isolation de la colonne "Surface (km2)" et conversion en liste Python
surfaces = list(iles["Surface (km²)"])

# Cast en float
surfaces = [float(x) for x in surfaces if not np.isnan(x)]

# Ajout des continents
surfaces.append(float(85545323))
surfaces.append(float(37856841))
surfaces.append(float(7768030))
surfaces.append(float(7605049))

# Classement décroissant
surfaces = ordreDecroissant(surfaces)

# Loi rang-taille
rangs = list(range(1, len(surfaces) + 1))

# Visualisation simple (illisible volontairement)
plt.figure()
plt.plot(rangs, surfaces, "o")
plt.title("Loi rang-taille des îles")
plt.xlabel("Rang")
plt.ylabel("Surface")
plt.savefig("./images/rang_taille_iles.png")
plt.close()

# Conversion logarithmique
log_rangs = conversionLog(rangs)
log_surfaces = conversionLog(surfaces)

# Visualisation log-log
plt.figure()
plt.plot(log_rangs, log_surfaces, "o")
plt.title("Loi rang-taille des îles (log-log)")
plt.xlabel("log(Rang)")
plt.ylabel("log(Surface)")
plt.savefig("./images/rang_taille_iles_loglog.png")
plt.close()

# COMMENTAIRE QUESTION 7 :
# Il n’est pas possible de réaliser un test de corrélation ou de concordance des rangs
# car il n’existe ici qu’un seul classement (les surfaces). Les tests de Spearman et
# Kendall nécessitent la comparaison de deux classements distincts.



# =================================
# Partie sur la population mondiale
# =================================

monde = ouvrirUnFichier("./data/Le-Monde-HS-Etats-du-monde-2007-2025.csv")

# Isolation des colonnes et conversion en listes Python
etat = list(monde["État"])

pop2007 = list(monde["Pop 2007"])
pop2025 = list(monde["Pop 2025"])
dens2007 = list(monde["Densité 2007"])
dens2025 = list(monde["Densité 2025"])

# Classements décroissants
ordre_pop2007 = ordrePopulation(pop2007, etat)
ordre_pop2025 = ordrePopulation(pop2025, etat)
ordre_dens2007 = ordrePopulation(dens2007, etat)
ordre_dens2025 = ordrePopulation(dens2025, etat)

# Comparaison population / densité
classement_2007 = classementPays(ordre_pop2007, ordre_dens2007)
classement_2025 = classementPays(ordre_pop2025, ordre_dens2025)

# Tri selon le classement population
classement_2007.sort()
classement_2025.sort()

# Séparation en deux listes (boucle obligatoire)
rang_pop_2007 = []
rang_dens_2007 = []

for element in classement_2007:
    rang_pop_2007.append(element[0])
    rang_dens_2007.append(element[1])

rang_pop_2025 = []
rang_dens_2025 = []

for element in classement_2025:
    rang_pop_2025.append(element[0])
    rang_dens_2025.append(element[1])

# Tests statistiques
spearman_2007 = scipy.stats.spearmanr(rang_pop_2007, rang_dens_2007)
kendall_2007 = scipy.stats.kendalltau(rang_pop_2007, rang_dens_2007)

spearman_2025 = scipy.stats.spearmanr(rang_pop_2025, rang_dens_2025)
kendall_2025 = scipy.stats.kendalltau(rang_pop_2025, rang_dens_2025)

print("2007 - Spearman :", spearman_2007)
print("2007 - Kendall :", kendall_2007)
print("2025 - Spearman :", spearman_2025)
print("2025 - Kendall :", kendall_2025)


# =========================
# Partie bonus
# =========================

def analyseClassement(classement):
    rang1 = []
    rang2 = []
    for element in classement:
        rang1.append(element[0])
        rang2.append(element[1])
    return scipy.stats.spearmanr(rang1, rang2), scipy.stats.kendalltau(rang1, rang2)

# Exemple d'utilisation
analyse_2007 = analyseClassement(classement_2007)
analyse_2025 = analyseClassement(classement_2025)
