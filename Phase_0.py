import spacy, bs4 as BeautifulSoup

#Chargement de Spacy
#Le Natural Language Processing (traitement automatique du langage naturel) 
#a permis l’émergence d’outils de traduction automatique, de génération de texte
#ou encore de classification de documents.

nlp = spacy.load('fr')
print("spacy chargé")

import time
t = time.time()
t2 = 0
for k in range(10):
    dictionnaireWiki = {}
    #len(os.listdir('page4/')) donne le nombre de fichier du répertoire
    for NumPage in range(1,2):
        #Ouverture en lecture de tous les fichiers du dossier des articles
        fichierR = open('page4/'+str(NumPage)+'.txt', 'r', encoding = 'utf-8')
        lireFichier = fichierR.read()
        #Je retire les tags pour alléger le contenu
        soup = BeautifulSoup.BeautifulSoup(lireFichier, "lxml").get_text()
        fichierR.close()
        #Ouverture en écriture de tous les fichiers du dossier des articles
        fichier = open('page4/'+str(NumPage)+'clean.txt', 'w', encoding = 'utf-8')
        t3 = time.time()
        document = nlp(soup)
        t2 += time.time() - t3
        #Je ne veux garder que les mots qui sont des noms et qui ont plus de 2 lettres
        for mot in document:
            #pos [Parts of Speech] tagging detection
            if mot.pos_ == 'NOUN' and len(mot) > 1:
                #tokenization
                #étape pas nécessaire pour toi, faut pas réécrire le fichier xD
                fichier.write(mot.text+" ")
                #j'ajoute les mots au dictionnaires avec un tuple vide pour plusieurs clés
                if mot.text not in dictionnaireWiki:
                    dictionnaireWiki[mot.text] = {}
                    dictionnaireWiki[mot.text][NumPage] = 1
                else :
                    if NumPage in dictionnaireWiki[mot.text]:
                        dictionnaireWiki[mot.text][NumPage] += 1
                    else:
                        dictionnaireWiki[mot.text][NumPage] = 1
        fichier.close()

t = time.time()-t
print(t)
