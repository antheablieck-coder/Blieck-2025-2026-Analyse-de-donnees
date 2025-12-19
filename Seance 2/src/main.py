#coding:utf8

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Source des données : https://www.data.gouv.fr/datasets/election-presidentielle-des-10-et-24-avril-2022-resultats-definitifs-du-1er-tour/


# Mettre dans un commentaire le numéro de la question

# Question 5
data = pd.DataFrame(contenu)
print(data.head)

# Question 6
print ("nombre de lignes: ",len(contenu))
print ("nombre de colonnes: ",len(contenu.columns))
# Question 7
print(contenu.dtypes)
# Questions 8 et 9
print ("nombre d'inscrits: ",format(contenu["Inscrits"].sum(),",").replace(","," "))
# Question 10
effectifs =[]
for colonne in contenu: 
    if contenu.dtypes [colonne] !=object:   
        effectifs.append (int(contenu [colonne].sum()))
print (effectifs)

# Question 11
inscrit =[]
for departement in contenu ["Inscrits"]:
    inscrit.append (departement)

votant=[]
for departement in contenu ["Votants"]:
    votant.append (departement)
    
nom=[]
for departement in contenu ["LibellÃ© du dÃ©partement"]:
    nom.append (departement)


for ins,vot,n in zip(inscrit,votant,nom):
  print (ins,vot,n)
  plt.figure()
  a=np.array (["Inscrits","Votants"])
  b=np.array ([ins,vot])
  plt.bar (a,b)
  plt.title (n)
  plt.savefig ("diagrammes en barres/"+n.replace("/"," ")+".png")
  plt.close()

#Question 12
blanc=[]
for departement in contenu ["Blancs"]:
    blanc.append (departement)

nul=[]
for departement in contenu ["Nuls"]:
    nul.append (departement)
    
exprime=[]
for departement in contenu ["ExprimÃ©s"]:
    exprime.append (departement)
    
abstention=[]
for departement in contenu ["Abstentions"]:
    abstention.append (departement)
    
#for b,nu,e,a,n in zip(blanc,nul,exprime,abstention,nom):
   plt.figure()
   valeur=[b,nu,e,a]
   label=["Blancs","Nuls","Exprimés","Abstentions"]
   plt.pie (valeur,labels=label)
   plt.title (n)
   plt.savefig ("diagrammes circulaire/"+n.replace("/"," ")+".png")
   plt.close()
    
#Question 13
for b,nu,e,a,n,ins in zip(blanc,nul,exprime,abstention,nom,inscrit):
    plt.figure()
   y=np.array([(a/ins)*100,(b/ins)*100,(nu/ins)*100,(e/ins)*100])
   x=np.array(["Abstentions","Blancs","Nuls","Exprimés"])
   plt.bar (x,y)
   plt.title (n)
   plt.ylabel("(%)")
   plt.savefig ("histogrammes/"+n.replace("/"," ")+".png")
   plt.close()

#Question bonus

Arthaud=[]
for departement in contenu ["Voix"]:
    Arthaud.append (departement)
    
Roussel=[]
for departement in contenu ["Voix.1"]:
    Roussel.append (departement)   

Macron=[]
for departement in contenu ["Voix.2"]:
    Macron.append (departement)
    
Lassalle=[]
for departement in contenu ["Voix.3"]:
    Lassalle.append (departement)
    
Lepen=[]
for departement in contenu ["Voix.4"]:
    Lepen.append (departement)
    
Zemmour=[]
for departement in contenu ["Voix.5"]:
    Zemmour.append (departement)
    
Melenchon=[]
for departement in contenu ["Voix.6"]:
    Melenchon.append (departement)

Hidalgo=[]
for departement in contenu ["Voix.7"]:
    Hidalgo.append (departement)
    
Jadot=[]
for departement in contenu ["Voix.8"]:
    Jadot.append (departement)

Pecresse=[]
for departement in contenu ["Voix.9"]:
    Pecresse.append (departement)

Poutou=[]
for departement in contenu ["Voix.10"]:
    Poutou.append (departement)
    
Dupont=[]
for departement in contenu ["Voix.11"]:
    Dupont.append (departement)
    
for (arthaud,roussel,macron,lassalle,lepen,zemmour,melenchon,hidalgo,jadot,pecresse,poutou,dupont,n) in zip(Arthaud,Roussel,Macron,Lassalle,Lepen,Zemmour,Melenchon,Hidalgo,Jadot,Pecresse,Poutou,Dupont,nom):
    plt.figure()
    a=[arthaud,roussel,macron,lassalle,lepen,zemmour,melenchon,hidalgo,jadot,pecresse,poutou,dupont]
    b=["Arthaud","Roussel","Macron","Lassalle","Lepen","Zemmour","Melenchon","Hidalgo","Jadot","Pecresse","Poutou","Dupont"]
    plt.pie (a,labels=b)
    plt.title (n)
    plt.savefig ("bonus/"+n.replace("/"," ")+".png")
    plt.close()
    
plt.figure()
a=[sum(Arthaud),sum(Roussel),sum(Macron),sum(Lassalle),sum(Lepen),sum(Zemmour),sum(Melenchon),sum(Hidalgo),sum(Jadot),sum(Pecresse),sum(Poutou),sum(Dupont)]
b=["Arthaud","Roussel","Macron","Lassalle","Lepen","Zemmour","Melenchon","Hidalgo","Jadot","Pecresse","Poutou","Dupont"]
plt.pie(a,labels=b)
plt.title("Total France")
plt.savefig ("bonus/Total.png")
plt.close()
    










