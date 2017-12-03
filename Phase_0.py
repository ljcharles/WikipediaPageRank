import bs4 as BeautifulSoup, nltk, time, threading, pickle 
#Le Natural Language Processing (traitement automatique du langage naturel) 
#a permis l’émergence d’outils de traduction automatique, de génération de texte
#ou encore de classification de documents.

dictionnaireWiki = {}

def faireDictionnaire(pageDepart,pageArrivee):
    #listeDeCharAsuppr = ["[", "]", "'", "|", "=", "//", "/"]
    #pageDepart = 1
    #pageArrivee = 2
    pageArrivee += 1
    t = time.time()
    
    for NumPage in range(pageDepart,pageArrivee):
        #Ouverture en lecture de tous les fichiers du dossier des articles
        fichierR = open('pageClean/'+str(NumPage)+'.txt', 'r', encoding = 'utf-8')
        lireFichier = fichierR.read()
        
        #Je retire les tags pour alléger le contenu
       # soup = BeautifulSoup.BeautifulSoup(lireFichier, "lxml").get_text()
        fichierR.close()
        
        #Ouverture en écriture de tous les fichiers du dossier des articles
        #fichier = open('pageClean/'+str(NumPage)+'.txt', 'w', encoding = 'utf-8')
        #document = nltk.word_tokenize(soup, language='french')
        document = nltk.word_tokenize(lireFichier, language='french')
        tags = nltk.pos_tag(document)
        taille = len(tags) - 1
    
        #Je ne veux garder que les mots qui sont des noms et qui ont plus d' 1 lettre
        for i in range(0, taille):
            mot = tags[i][0]
            premiereLettreTag = tags[i][1][0]
            
            """for char in listeDeCharAsuppr:
                if char in mot:
                    mot = mot.replace(char, " ")"""
                    
            #pos [Parts of Speech] tagging detection
            if  premiereLettreTag == 'N' and len(mot) > 1 :
                #fichier.write(mot+" ")
                #j'ajoute les mots au dictionnaires avec un tuple vide pour plusieurs clés
                if mot not in dictionnaireWiki:
                    dictionnaireWiki[mot] = {}
                    dictionnaireWiki[mot][NumPage] = 1
                else :
                    if NumPage in dictionnaireWiki[mot]:
                        dictionnaireWiki[mot][NumPage] += 1
                    else:
                        dictionnaireWiki[mot][NumPage] = 1
        
        #fichier.close()
    t = time.time()-t
    #print(t)

thread = [None] * 11
thread[0] = threading.Thread(target = faireDictionnaire, args = (      0,    400000))
thread[1] = threading.Thread(target = faireDictionnaire, args = (    400001,    400500))
thread[2] = threading.Thread(target = faireDictionnaire, args = (    400501,   400700))
thread[3] = threading.Thread(target = faireDictionnaire, args = (   400701,   400800))
thread[4] = threading.Thread(target = faireDictionnaire, args = (   400801,   400900))
thread[5] = threading.Thread(target = faireDictionnaire, args = (   400901,  410500))
thread[6] = threading.Thread(target = faireDictionnaire, args = (  410501,  420500))
thread[7] = threading.Thread(target = faireDictionnaire, args = (  420501,  440500))
thread[8] = threading.Thread(target = faireDictionnaire, args = (  440501, 460500))
thread[9] = threading.Thread(target = faireDictionnaire, args = ( 460501, 480500))
thread[10] = threading.Thread(target = faireDictionnaire, args = (480501, 500000))

for i in range(len(thread)):
    thread[i].start()
for i in range(len(thread)):
    thread[i].join()
    
fichierDico = open('pageClean/dictionnaire.pickle', 'wb', encoding = 'utf-8')
#fichierDico.write(str(dictionnaireWiki))
pickle.dump(dictionnaireWiki,fichierDico)
fichierDico.close()
